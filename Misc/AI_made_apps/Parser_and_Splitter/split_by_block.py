#!/usr/bin/env python3
"""
結合済みのテキストファイルを、指定サイズ（デフォルト1MB）以下になるように
ブロック区切り（--- path ---）で安全に分割する。
"""

import os
import sys

# ------------------------------------------------------------
# 設定
# ------------------------------------------------------------
MAX_SIZE = 1_048_576  # 1 MB

def split_file(input_path, output_prefix="split_part", max_size=MAX_SIZE):
    """ブロック境界を守りながらファイルを分割する"""
    if not os.path.isfile(input_path):
        print(f"Error: '{input_path}' not found.")
        return

    part_num = 1
    current_size = 0
    current_content = []

    def write_part(content_lines):
        """現在の内容をパートファイルに書き出す"""
        nonlocal part_num
        out_filename = f"{output_prefix}_{part_num:04d}.txt"
        with open(out_filename, 'w', encoding='utf-8') as f:
            f.writelines(current_content)
        print(f"Written: {out_filename} ({len(current_content)} lines)")
        part_num += 1

    with open(input_path, 'r', encoding='utf-8') as f:
        block_lines = []
        in_block = False

        for line in f:
            # ブロック開始マーカーを検出
            if line.startswith('--- ') and line.rstrip().endswith(' ---'):
                # 前のブロックが存在すれば、それを現在のパートに追加試行
                if block_lines:
                    block_text = ''.join(block_lines)
                    block_size = len(block_text.encode('utf-8'))
                    # もし現在のパートに追加してもサイズ超過しないか？
                    if current_size + block_size <= max_size:
                        current_content.extend(block_lines)
                        current_size += block_size
                    else:
                        # 超過する場合は現在のパートを書き出してリセット
                        if current_content:
                            write_part(current_content)
                            current_content = []
                            current_size = 0
                        # 新しいパートにブロックを追加
                        current_content.extend(block_lines)
                        current_size = block_size
                    block_lines = []
                # 新しいブロックの開始行として追加
                block_lines.append(line)
            else:
                block_lines.append(line)

        # 最後のブロックを処理
        if block_lines:
            block_text = ''.join(block_lines)
            block_size = len(block_text.encode('utf-8'))
            if current_size + block_size <= max_size:
                current_content.extend(block_lines)
                current_size += block_size
            else:
                if current_content:
                    write_part(current_content)
                    current_content = []
                current_content.extend(block_lines)
                current_size = block_size

    # 残りを書き出し
    if current_content:
        write_part(current_content)

    print("Split completed.")

# ------------------------------------------------------------
# エントリポイント
# ------------------------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python split_by_block.py <input_file> [output_prefix] [max_size_mb]")
        print("Example: python split_by_block.py combined.txt part 1")
        sys.exit(1)

    input_file = sys.argv[1]
    prefix = sys.argv[2] if len(sys.argv) >= 3 else "split_part"
    if len(sys.argv) >= 4:
        try:
            max_mb = float(sys.argv[3])
            max_bytes = int(max_mb * 1_048_576)
        except ValueError:
            print("Error: max_size_mb must be a number.")
            sys.exit(1)
    else:
        max_bytes = MAX_SIZE

    split_file(input_file, prefix, max_bytes)