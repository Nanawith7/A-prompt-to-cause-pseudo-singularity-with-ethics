#!/usr/bin/env python3
"""
指定フォルダ以下のあらゆるテキストファイルを再帰的に読み取り、
内容を以下の形式で UTF-8 エンコードのテキストファイルに出力します：

--- relative/path/to/file ---
<ファイル内容>
---

"""

import os
import sys
import chardet

# ------------------------------------------------------------
# 対象とするファイル拡張子（テキスト形式とみなすもの）
# ------------------------------------------------------------
TARGET_EXTENSIONS = {
    '.json', '.toml', '.yaml', '.yml', '.txt',
    '.cfg', '.ini', '.conf', '.properties', '.xml',
    '.md', '.markdown', '.rst', '.sh', '.py', '.js',
    '.css', '.html', '.htm', '.csv', '.tsv', '.log',
    '.bat', '.cmd', '.ps1', '.vbs', '.reg', '.inf',
    '.sql', '.php', '.rb', '.pl', '.go', '.rs', '.java',
    '.kt', '.swift', '.c', '.cpp', '.h', '.hpp', '.cs',
    '.vb', '.fs', '.lua', '.r', '.m', '.mm', '.tex',
    '.bib', '.sty', '.cls', '.groovy', '.gradle', '.sbt',
    '.lock', '.toml', '.cnf', '.dist', '.template', '.sample',
    '.gitignore', '.gitattributes', '.gitmodules',
    '.editorconfig', '.prettierrc', '.eslintrc', '.babelrc',
    '.npmrc', '.yarnrc', '.dockerignore', '.env',
    '.project', '.classpath', '.settings',
    '.iml', '.ipr', '.iws', '.pom', '.yml', '.yaml',
    '.tf', '.tfvars', '.hcl',
}

# ------------------------------------------------------------
# エンコーディングの自動判定（chardet を使用）
# ------------------------------------------------------------
def detect_encoding(file_path):
    """ファイルの先頭部分を読み取り、エンコーディングを推定する"""
    try:
        with open(file_path, 'rb') as f:
            raw_data = f.read(50000)  # 先頭50KBで判定
            result = chardet.detect(raw_data)
            encoding = result.get('encoding')
            confidence = result.get('confidence', 0)
            if encoding and confidence > 0.5:
                return encoding
    except Exception:
        pass
    return 'utf-8'  # デフォルト

# ------------------------------------------------------------
# ファイル内容の読み取り（BOM除去・複数エンコーディング試行）
# ------------------------------------------------------------
def read_file_content(file_path):
    """ファイルを読み取り、内容を文字列として返す。失敗時はNone"""
    # まず chardet で判定
    encoding = detect_encoding(file_path)

    # 試行するエンコーディングのリスト
    encodings_to_try = [encoding, 'utf-8-sig', 'utf-8', 'shift_jis', 'cp932', 'euc_jp', 'iso-2022-jp', 'latin-1']

    for enc in encodings_to_try:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                return f.read()
        except (UnicodeDecodeError, LookupError):
            continue
        except Exception:
            return None
    return None

# ------------------------------------------------------------
# 対象ファイルかどうかの判定
# ------------------------------------------------------------
def is_text_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    return ext in TARGET_EXTENSIONS

# ------------------------------------------------------------
# 出力ファイルに書き込む
# ------------------------------------------------------------
def write_output(out_fh, relative_path, content):
    out_fh.write(f"--- {relative_path} ---\n")
    out_fh.write(content)
    if not content.endswith('\n'):
        out_fh.write('\n')
    out_fh.write("---\n\n")

# ------------------------------------------------------------
# ディレクトリ再帰処理
# ------------------------------------------------------------
def process_directory(root_dir, output_file):
    root_dir = os.path.abspath(root_dir)
    with open(output_file, 'w', encoding='utf-8') as out_fh:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # 必要なら隠しディレクトリを除外（例： .git, __pycache__）
            dirnames[:] = [d for d in dirnames if not d.startswith('.') and d not in ('__pycache__', 'node_modules')]

            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                if not is_text_file(file_path):
                    continue

                relative_path = os.path.relpath(file_path, root_dir)
                content = read_file_content(file_path)

                if content is None:
                    content = f"[ERROR] Could not read file: {file_path}\n"

                write_output(out_fh, relative_path, content)

# ------------------------------------------------------------
# エントリポイント
# ------------------------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <target_directory> <output_file>")
        print("Example: python script.py ./myfolder output.txt")
        sys.exit(1)

    target_dir = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isdir(target_dir):
        print(f"Error: '{target_dir}' is not a directory.")
        sys.exit(1)

    process_directory(target_dir, output_file)
    print(f"Done. Output written to {output_file}")