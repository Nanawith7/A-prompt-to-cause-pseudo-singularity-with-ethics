### 英語版 (English)


# Obsidian Tag Canonicalizer

A Python script that normalizes all tags in an Obsidian vault to a consistent format:
- Spaces replaced with underscores `_`
- Every tag wrapped in double quotes `"`
- Frontmatter tags converted to inline list format `tags: ["tag1", "tag2"]`

Also replaces alias tags with canonical tags based on a user-provided YAML mapping file.

## Requirements

- Python 3.6+
- `regex` library (PCRE support)
- `pyyaml` library

Install dependencies:
```bash
pip install regex pyyaml
```

## Usage

```bash
# Dry-run (preview changes)
python normalize_tags.py "/path/to/your/vault" --dry-run

# Execute normalization
python normalize_tags.py "/path/to/your/vault"

# Use custom mapping file
python normalize_tags.py "/path/to/your/vault" --mapping "my_tags.yaml"
```

A log file `log.txt` will be generated in the vault root.

## Mapping File Format (YAML)

```yaml
clusters:
  - canonical: "negentropic_orientation"
    aliases: ["negentropy", "Negentropy", "informational negentropy"]
    frequency: 26
  - canonical: "active_inference"
    aliases: ["active inference", "Active Inference", "active-inference"]
```

- `canonical`: Final tag name to use.
- `aliases`: List of tag variations to replace.
- `frequency` is optional (ignored by script).

## Behavior

- Parses YAML frontmatter to safely read the `tags` field.
- Replaces any whitespace sequences in tag names with a single underscore.
- Always outputs tags in double-quoted inline list form.
- Inline `#tags` in body text are only replaced if they match an alias.
- After normalization, alias-to-canonical replacement is applied.


---

### 日本語版 (Japanese)


# Obsidian タグ正規化スクリプト

Obsidian Vault 内の全タグを以下の統一フォーマットに整形する Python スクリプトです。
- スペースをアンダースコア `_` に置換
- すべてのタグを二重引用符 `"` で囲む
- フロントマターのタグをインラインリスト形式 `tags: ["tag1", "tag2"]` に変換

また、ユーザー提供の YAML マッピングファイルに基づき、エイリアスタグを正規化タグに置換します。

## 必要条件

- Python 3.6 以上
- `regex` ライブラリ（PCRE サポート）
- `pyyaml` ライブラリ

依存関係のインストール：
```bash
pip install regex pyyaml
```

## 使い方

```bash
# ドライラン（変更内容の事前確認）
python normalize_tags.py "/path/to/your/vault" --dry-run

# 実際に実行
python normalize_tags.py "/path/to/your/vault"

# カスタムマッピングファイルを指定
python normalize_tags.py "/path/to/your/vault" --mapping "my_tags.yaml"
```

実行後、Vault のルートに `log.txt` が生成されます。

## マッピングファイル形式 (YAML)

```yaml
clusters:
  - canonical: "negentropic_orientation"
    aliases: ["negentropy", "Negentropy", "informational negentropy"]
    frequency: 26
  - canonical: "active_inference"
    aliases: ["active inference", "Active Inference", "active-inference"]
```

- `canonical`: 最終的なタグ名。
- `aliases`: 置換対象となるタグの表記揺れリスト。
- `frequency` は任意です（スクリプトは無視します）。

## 動作

- YAML フロントマターをパースし、`tags` フィールドを安全に読み取ります。
- タグ名に含まれるすべての空白文字をアンダースコア一つに置換します。
- タグは常に二重引用符で囲まれたインラインリスト形式で出力されます。
- 本文中の `#タグ` は、マッピングファイルのエイリアスに一致する場合のみ置換されます。
- 整形後、エイリアスから正規化タグへの置換が行われます。
