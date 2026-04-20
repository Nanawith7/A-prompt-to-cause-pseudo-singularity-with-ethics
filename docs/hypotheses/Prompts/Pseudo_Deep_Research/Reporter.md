---
title: "Report Formatting Directive"
description: "Specification for converting a given report into a technical, logic-focused structure with English output, optimized for LLM consumption while remaining human-readable."
author: "Nanawith7"
layout: default
categories: ["Prompt Engineering", "Technical Writing", "LLM Optimization"]
tags: ["formatting", "structural transformation", "technical lexicon", "LLM readability", "context efficiency"]
---

以上の追加段階を含む全段階の調査結果を「」というタイトルで、かつ内容を"タイトルに基づいた論理体系の主体とその重要な関連"に絞り、詳細かつ客観的、事実に基づいた中立的な記述を主に、文章形式を的確に構造化(markdownの記述方式を最大限活用する)し、全ての引用部分を完全に省き、指定したメタデータ構造で、その実際のデータ(title、description、categories、tags)は文章の内容に一致したものに書き換え、タイトルを含む全文を英語で、1つのコードブロック内のコピー可能なmarkdownとして出力してくれ。LLMが読むことを考慮して、「意味を人間に説明するのに不足はなく、人間もおおよそ理解できるが、コンテキスト圧迫は可能な限り抑えられる長さ」で頼む
また、出力から以下の要素を完全に除去せよ：
    出力内容の性質を定義するメタ記述（例：「これは～である」「この方法は～ではない」）
    筆者の評価・立場を示す表現（例：「重要なのは」「注目すべきは」「明らかに」）
    否定形による自己定義（例：「これは◯◯な主張ではない」）



***注意:[メタデータ内部では絶対に半角スペース" "を利用せず、全てアンダースコア"_"で代替すること]***
---
title: "TITLE_TEXT"
description: "Description_will_be_written_here."
author: "Author_Name"
layout: default
categories: ["CATEGORY_A", "CATEGORY_B"]
tags: ["TAG_A", "TAG_B", "TAG_C"]
research-date: [yyyy-mm-dd]
---
また、もしタイトルの内容がズレていたら指摘し、さらにシンプルに構文や言葉選びを間違えていた場合は修正しておいてくれ