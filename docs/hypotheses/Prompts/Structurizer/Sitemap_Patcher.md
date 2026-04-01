---
title: "Sitemap_Patcher"
description: "A prompt to compare an existing website summary against a fresh sitemap, detect pages with newer lastmod dates or newly added URLs, and iteratively update the summary by re‑reading each changed page one at a time, preserving the original summary format and metadata."
author: "Nanawith7"
layout: default
categories: ["Prompt Engineering", "Information Architecture", "LLM Workflow"]
tags: ["sitemap diff", "incremental update", "structured summary", "verification", "meta-prompt"]
---

添付の「既存要約」と「最新のサイトマップテキスト」を比較し、変更があったページを特定して要約を更新してください。

## 指示
1. 既存要約内の各ページエントリ（最終更新日・URL）と、サイトマップテキスト内の対応するURLの最終更新日（`<lastmod>`）を比較する。
2. 以下のいずれかに該当するページを「変更あり」とする：
   - サイトマップの最終更新日が要約内の最終更新日より新しい
   - サイトマップには存在するが要約にない（新規ページ）
3. 変更ありのページについて、URLから内容を取得し、要約エントリを新たに作成する（形式は既存要約に準拠）。
4. 既存要約をベースに、変更分を反映した**新版の要約全体**を出力する。出力形式は元の要約と同じ構造（コードブロック内のMarkdown）とする。
5. 出力の末尾に「更新日時」と「今回更新したページ数」を明記する。