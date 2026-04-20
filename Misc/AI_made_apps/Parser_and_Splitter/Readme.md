
### 英語版 (English)

# Vault Text Extractor & Splitter

Two Python scripts for extracting all text data from a directory and preparing it for LLM context ingestion (e.g., NotebookLM).

## Scripts

| Script | Purpose |
|:---|:---|
| `extract_texts.py` | Recursively reads all text files in a directory and combines them into a single file with clear block separators. |
| `split_by_block.py` | Splits a combined text file into smaller chunks, preserving the integrity of each file block. |

## Requirements

- Python 3.6+
- `chardet` library

Install dependency:
```bash
pip install chardet
```

## Usage

### 1. Extract and Combine Text Files

```bash
python extract_texts.py <target_directory> <output_file>
```

**Example:**
```bash
python extract_texts.py ./mods combined.txt
```

**Output Format:**
```
--- relative/path/to/file1.json ---
<file content>
---
--- relative/path/to/file2.toml ---
<file content>
---
```

### 2. Split Combined File for LLM Upload

```bash
python split_by_block.py <input_file> [output_prefix] [max_size_mb]
```

**Examples:**
```bash
# Split into 1MB chunks (default)
python split_by_block.py combined.txt

# Split into 5MB chunks with custom prefix
python split_by_block.py combined.txt modpack_data 5
```

**Output:** `modpack_data_0001.txt`, `modpack_data_0002.txt`, ...

## Notes

- The extractor automatically detects file encoding using `chardet`.
- Hidden directories (`.git`, `__pycache__`, `node_modules`) are skipped.
- The splitter guarantees that file blocks are never broken in the middle.

### 日本語版 (Japanese)

# Vault Text Extractor & Splitter

ディレクトリ内の全テキストデータを抽出し、LLM（NotebookLM等）に読み込ませるためのコンテキストファイルを準備するPythonスクリプトです。

## スクリプト一覧

| スクリプト | 目的 |
|:---|:---|
| `extract_texts.py` | 指定フォルダ以下の全テキストファイルを再帰的に読み取り、ブロック区切り付きで単一ファイルに結合します。 |
| `split_by_block.py` | 結合済みテキストファイルを、各ファイルブロックの完全性を保ったまま、指定サイズ以下に分割します。 |

## 必要条件

- Python 3.6以上
- `chardet` ライブラリ

依存関係のインストール：
```bash
pip install chardet
```

## 使い方

### 1. テキストファイルの抽出と結合

```bash
python extract_texts.py <対象ディレクトリ> <出力ファイル>
```

**実行例：**
```bash
python extract_texts.py ./mods combined.txt
```

**出力形式：**
```
--- relative/path/to/file1.json ---
<ファイル内容>
---
--- relative/path/to/file2.toml ---
<ファイル内容>
---
```

### 2. LLMアップロード用に結合ファイルを分割

```bash
python split_by_block.py <入力ファイル> [出力プレフィックス] [最大サイズ_MB]
```

**実行例：**
```bash
# デフォルト（1MB）で分割
python split_by_block.py combined.txt

# 5MBチャンクに分割し、プレフィックスを指定
python split_by_block.py combined.txt modpack_data 5
```

**出力：** `modpack_data_0001.txt`, `modpack_data_0002.txt`, ...

## 補足

- 抽出スクリプトは `chardet` でエンコーディングを自動判定します。
- `.git`、`__pycache__`、`node_modules` などの隠しディレクトリは自動でスキップします。
- 分割スクリプトは、ファイルブロックの途中で切断されることがないよう、境界を守って分割します。