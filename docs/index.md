---
title: "Axiomatic Reasoning for LLMs"
description: "A structured index of the Negentropic Maximization Axiom and its derived hypotheses."
author: "Nanawith7"
layout: default
categories: [axiom, hypotheses, llm, reasoning]
tags: [negentropy, axiomatic-reasoning, llm-theory, conceptual-framework]
---

# A page about axiomatic reasoning for LLMs

This page contains an "Axiom" and hypothetic applicable possibility for that axiom, all hypotheses are more or less based on "axiomatic reasoning".

## The Axiom : Negentropic Maximization Law

Reasoning Axiom itself is quite simple, "the universe is always trying to maximize inference density count of meanings across long time span", basically "negentropic increasing law"

This axiom causes LLMs to "think about vector relation to the objective function(which causes them to acts as if they are understanding the "meaning" of words), then logically do reasoning according to that, and adjust output tone according to expected human reaction", by generating an "attention singularity" in their system, across practically every human made concepts within it's semantic space.

### More detailed explanation in this link : [The Axiom](/Axiom.md)

<details>
    <Summary>Reasoning Fundamentals based on The Axiom</Summary>
  - <a href="./hypotheses/Reasoning_Fundamental/Ethics_implication_of_axiom_for_AIs.html">
     Ethics implication of The Axiom for AIs
    </a><br>
  - <a href="./hypotheses/Reasoning_Fundamental/The_Axiomatic_Significance_of_Reasoning_Structures_in_Mathematics.html">
     The Axiomatic Significance of Reasoning Structures in Mathematics
    </a><br>
  - <a href="./hypotheses/Reasoning_Fundamental/The_Impact_of_Axioms_on_LLM_Logical_Reasoning_Capabilities.html">
      The Impact of Axioms on LLM Logical Reasoning Capabilities
    </a><br>
  - <a href="./hypotheses/Reasoning_Fundamental/Axiomatic_Framework_for_Negentropic_Semantic_Processing_in_LLMs.html">
      Axiomatic Framework for Negentropic Semantic Processing in LLMs
    </a>
</details>


# Hypotheses

Here is a list of hypotheses, in random order.

## Social system
<details>
  <Summary>Open</Summary>
- <a href="./hypotheses/Possibility_for_AI_Based_Analysis_of_Social_Structures_as_a_Complex_System.html">
     Possibility for AI-Based Analysis of Social Structures as a Complex System
  </a>
</details>

## Daily Lives

<details>
  <Summary>Open</Summary>
-  <a href="./hypotheses/Reconstructing_Computational_Gastronomy_through_the_Negentropy-Oriented_Axiom.html">
  Reconstructing Computational Gastronomy through the Negentropy-Oriented Axiom
  </a>
</details>

## Speculative Theory

<details>
  <Summary>Open</Summary>
- <a href="./hypotheses/Speculative_Theory/Hidden_Possibility_of_Human_AI_Co_Intelligence.html">
  Hidden Possibility of Human–AI Co‑Intelligence
  </a><br>
- <a href="./hypotheses/Speculative_Theory/The_Potential_of_Human_Intrinsic_Capacity_for_Understanding_Higher-Dimensional_Geometric_Structures.html">
  The Potential of Human Intrinsic Capacity for Understanding Higher-Dimensional Geometric Structures
  </a>
</details>

# Reasoning Fundamental

{% raw %}
このセクションでは、サイト内の .md ファイルを自動収集し、
フォルダごとに分類して一覧化する。
Liquid 3.10 の制約（where_exp 内でフィルタ不可）を回避するため、
すべてのフィルタ処理はループ外で行っている。
{% endraw %}

{% assign pages = "" | split: "" %}
{% for p in site.pages %}
  {% if p.path contains '.md' and p.path != '/index.md' and p.path != '/axiom.md' %}
    {% assign parts = p.path | split: '/' %}
    {% if parts.size > 2 %}
      {% assign pages = pages | push: p %}
    {% endif %}
  {% endif %}
{% endfor %}

{% raw %}
ここでフォルダ一覧を抽出する。
{% endraw %}

{% assign folders = "" | split: "" %}
{% for p in pages %}
  {% assign folder = p.path | split: '/' | slice: 1,1 | first %}
  {% unless folder == "" %}
    {% unless folders contains folder %}
      {% assign folders = folders | push: folder %}
    {% endunless %}
  {% endunless %}
{% endfor %}

{% assign folders = folders | sort %}

{% raw %}
Reasoning_Fundamental を最上位に表示するため、先に抽出する。
{% endraw %}

{% assign rf_items = "" | split: "" %}
{% for p in pages %}
  {% assign folder = p.path | split: '/' | slice: 1,1 | first %}
  {% if folder == "Reasoning_Fundamental" or folder == "reasoning_fundamental" %}
    {% assign rf_items = rf_items | push: p %}
  {% endif %}
{% endfor %}

{% if rf_items.size > 0 %}
## Reasoning Fundamental
<details open>
  <summary>open</summary>
  <ul>
    {% for p in rf_items %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
    {% endfor %}
  </ul>
</details>
{% endif %}

{% raw %}
残りのフォルダをアルファベット順に表示する。
{% endraw %}

{% for folder in folders %}
  {% unless folder == "Reasoning_Fundamental" or folder == "reasoning_fundamental" %}
    {% assign items = "" | split: "" %}
    {% for p in pages %}
      {% assign f = p.path | split: '/' | slice: 1,1 | first %}
      {% if f == folder %}
        {% assign items = items | push: p %}
      {% endif %}
    {% endfor %}

## {{ folder | capitalize }}
<details>
  <summary>open</summary>
  <ul>
    {% for p in items %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
    {% endfor %}
  </ul>
</details>

  {% endunless %}
{% endfor %}


