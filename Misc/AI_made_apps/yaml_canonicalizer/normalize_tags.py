#!/usr/bin/env python3
"""
Obsidian Vault Tag Normalizer (Unconditional rewrite version)

Features:
- Parses frontmatter YAML to get the 'tags' field.
- Formats EVERY tag into double-quoted, underscore-separated form.
- Unconditionally replaces the original tags: line(s) with a single inline list: tags: ["tag1", "tag2"]
- Replaces alias tags with canonical tags based on a YAML mapping file.
- Preserves inline #tags in body text (only replaces aliases, no quotes added).
- Outputs debug logs to both console and 'log.txt' file.
"""

import os
import sys
import regex as re
import yaml
import argparse
from pathlib import Path

# ----------------------------------------------------------------------
# Logging setup: tee output to both console and log file
# ----------------------------------------------------------------------
class Tee:
    def __init__(self, file_path, mode='w'):
        self.file = open(file_path, mode, encoding='utf-8')
        self.stdout = sys.stdout

    def write(self, message):
        self.stdout.write(message)
        self.file.write(message)

    def flush(self):
        self.stdout.flush()
        self.file.flush()

    def close(self):
        self.file.close()

log_tee = None

def log_print(*args, **kwargs):
    print(*args, **kwargs)

# ----------------------------------------------------------------------
DEBUG = True

def load_mapping(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    mapping = {}
    for cluster in data['clusters']:
        canonical = cluster['canonical']
        for alias in cluster['aliases']:
            if alias == canonical:
                continue
            mapping[alias] = canonical
    return mapping

def normalize_alias_pattern(alias):
    escaped = re.escape(alias)
    pattern = re.sub(r'\\[ _-]|[ _-]', r'[ _-]+', escaped)
    return pattern

def format_all_frontmatter_tags(content):
    """
    Unconditionally parse frontmatter, reformat the 'tags' list,
    and replace the original tags: line with a normalized inline list.
    """
    frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.search(frontmatter_pattern, content, flags=re.DOTALL)
    if not match:
        return content, False, "No frontmatter found"

    fm_text = match.group(1)
    try:
        fm_data = yaml.safe_load(fm_text)
        if fm_data is None:
            fm_data = {}
    except yaml.YAMLError as e:
        return content, False, f"YAML parse error: {e}"

    if 'tags' not in fm_data:
        return content, False, "No 'tags' field in frontmatter"

    tags = fm_data['tags']
    if isinstance(tags, str):
        tags = [tags]
    if not isinstance(tags, list):
        return content, False, f"Tags field is not a list: {type(tags)}"

    # Build normalized tags
    new_tags = []
    for tag in tags:
        if tag is None:
            continue
        tag_str = str(tag).strip()
        # Replace any whitespace sequence with underscore
        tag_str = re.sub(r'\s+', '_', tag_str)
        new_tags.append(f'"{tag_str}"')

    # Build replacement line
    replacement_line = 'tags: [' + ', '.join(new_tags) + ']'

    # Replace the original tags line(s)
    tags_line_pattern = r'^tags:\s*.*?(?=\n\S|\n---|$)'
    new_fm_text = re.sub(tags_line_pattern, replacement_line, fm_text, flags=re.MULTILINE | re.DOTALL)

    new_content = content[:match.start(1)] + new_fm_text + content[match.end(1):]
    return new_content, True, f"Replaced tags line with: {replacement_line}"

def normalize_content(content, mapping, file_path=""):
    # Step 1: Unconditionally format frontmatter tags
    content, fm_changed, fm_msg = format_all_frontmatter_tags(content)

    replacement_count = 0
    details = []
    flags = re.IGNORECASE | re.MULTILINE

    # Step 2: Inline #tags in body text
    for alias, canonical in mapping.items():
        alias_pattern = normalize_alias_pattern(alias)
        pattern = r'(?<!\w)#\K' + alias_pattern + r'(?!\w)'
        matches = list(re.finditer(pattern, content, flags=flags))
        if matches:
            content = re.sub(pattern, canonical, content, flags=flags)
            replacement_count += len(matches)
            details.append(f"  Inline #{alias} -> #{canonical} ({len(matches)} occurrences)")

    # Step 3: Frontmatter inline list (after formatting, all tags are quoted)
    for alias, canonical in mapping.items():
        alias_pattern = normalize_alias_pattern(alias)
        pattern = r'(?<=tags:\s*\[[^\]]*?(?:,|^)\s*)"?' + alias_pattern + r'"?\s*(?=(?:,|\]))'
        matches = list(re.finditer(pattern, content, flags=flags))
        if matches:
            content = re.sub(pattern, canonical, content, flags=flags)
            replacement_count += len(matches)
            details.append(f"  FM inline {alias} -> {canonical} ({len(matches)} occurrences)")

    # Step 4: Multi-line YAML tags (should not be needed after formatting)
    for alias, canonical in mapping.items():
        alias_pattern = normalize_alias_pattern(alias)
        pattern = r'(?<=^\s*-\s+)"?' + alias_pattern + r'"?\s*$'
        matches = list(re.finditer(pattern, content, flags=flags))
        if matches:
            content = re.sub(pattern, canonical, content, flags=flags)
            replacement_count += len(matches)
            details.append(f"  FM multiline {alias} -> {canonical} ({len(matches)} occurrences)")

    return content, replacement_count, details, fm_msg

def debug_sample_files(vault_path, max_files=5):
    log_print("\n[DEBUG] Sample file tag lines:")
    count = 0
    for md_file in Path(vault_path).rglob('*.md'):
        if count >= max_files:
            break
        log_print(f"\n--- {md_file} ---")
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    if '#' in line or 'tags:' in line.lower():
                        log_print(line.rstrip())
        except Exception as e:
            log_print(f"  [Error reading file: {e}]")
        count += 1

def process_vault(vault_path, mapping, dry_run=False):
    vault_path = Path(vault_path)
    total_files = 0
    updated_files = 0
    total_replacements = 0

    for md_file in vault_path.rglob('*.md'):
        total_files += 1
        if dry_run:
            log_print(f"[DRY RUN] Would process: {md_file}")
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            log_print(f"[ERROR] Could not read {md_file}: {e}")
            continue

        new_content, count, details, fm_msg = normalize_content(content, mapping, str(md_file))

        # We always print the file if frontmatter was changed, even if alias count = 0
        if count > 0 or "Replaced tags line" in fm_msg:
            log_print(f"\n📄 {md_file}")
            log_print(f"  FM action: {fm_msg}")
            for detail in details:
                log_print(detail)
            total_replacements += count
            updated_files += 1

            if not dry_run:
                try:
                    with open(md_file, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                except Exception as e:
                    log_print(f"[ERROR] Could not write {md_file}: {e}")

    log_print(f"\n{'='*50}")
    log_print(f"Total files scanned: {total_files}")
    log_print(f"Files updated: {updated_files}")
    log_print(f"Total alias replacements: {total_replacements}")

def main():
    global log_tee
    parser = argparse.ArgumentParser(description='Normalize Obsidian tags.')
    parser.add_argument('vault_path', help='Path to Obsidian vault')
    parser.add_argument('--mapping', default='canonical_tag.yaml', help='YAML mapping file')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    log_file_path = Path(args.vault_path) / 'log.txt'
    log_tee = Tee(str(log_file_path), 'w')
    sys.stdout = log_tee

    try:
        mapping = load_mapping(args.mapping)
        log_print(f"Loaded {len(mapping)} alias mappings.")

        if DEBUG:
            log_print("\n[DEBUG] Alias -> Canonical (first 10):")
            for alias, canonical in sorted(mapping.items())[:10]:
                log_print(f"  {alias} -> {canonical}")
            debug_sample_files(args.vault_path)

        process_vault(args.vault_path, mapping, args.dry_run)

        if args.dry_run:
            log_print("\n[DRY RUN] No files were changed.")
        else:
            log_print("\nTag normalization completed. Restart Obsidian to refresh cache.")
    finally:
        sys.stdout = sys.__stdout__
        log_tee.close()
        print(f"Log saved to {log_file_path}")

if __name__ == '__main__':
    main()