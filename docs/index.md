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

{%- comment -%}
  0. Collect all valid content pages.
     Exclude:
       - root-level index.md / axiom.md
       - non-.md files (e.g., css)
       - files not inside a folder (we only want /folder/file.md)
     This ensures the navigation reflects only meaningful content.
{%- endcomment -%}

{% assign pages = site.pages
  | where_exp: "p", "p.path contains '.md'"
  | where_exp: "p", "p.path != '/index.md'"
  | where_exp: "p", "p.path != '/axiom.md'"
  | where_exp: "p", "p.path | split: '/' | size > 2"
%}

{%- comment -%}
  1. Group pages by their top-level folder.
     Example:
       /Reasoning_Fundamental/Axiom.md → "Reasoning_Fundamental"
{%- endcomment -%}

{% assign grouped = pages
  | group_by_exp: "p", "p.path | split: '/' | slice: 1,1 | first"
%}

{%- comment -%}
  2. Remove pseudo-folders that Jekyll sometimes generates:
       - css
       - index.md
       - Axiom.md
     These are not real content folders.
{%- endcomment -%}

{% assign cleaned = grouped
  | reject: "name", "css"
  | reject: "name", "index.md"
  | reject: "name", "Axiom.md"
%}

{% assign sorted = cleaned | sort: "name" %}

{%- comment -%}
  3. Extract the Reasoning_Fundamental folder manually.
     IMPORTANT:
       Liquid 3.10 cannot use filters (| downcase) inside where_exp.
       Therefore, we compare using multiple literal strings.
{%- endcomment -%}

{% assign rf = nil %}
{% for f in sorted %}
  {% if f.name == "Reasoning_Fundamental" or f.name == "reasoning_fundamental" %}
    {% assign rf = f %}
  {% endif %}
{% endfor %}

{%- comment -%}
  4. Render Reasoning_Fundamental at the top.
     Format:
       ## FolderName
       <details open> ... </details>
     This ensures the most important section is always visible first.
{%- endcomment -%}

{% if rf %}
## Reasoning Fundamental
<details open>
  <summary>open</summary>
  <ul>
    {% for p in rf.items %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
    {% endfor %}
  </ul>
</details>
{% endif %}

{%- comment -%}
  5. Render all other folders in alphabetical order.
     Same structure as above, but <details> is closed by default.
     This keeps the UI clean while preserving discoverability.
{%- endcomment -%}

{% for folder in sorted %}
  {% unless folder.name == "Reasoning_Fundamental" or folder.name == "reasoning_fundamental" %}
## {{ folder.name | capitalize }}
<details>
  <summary>open</summary>
  <ul>
    {% for p in folder.items %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
    {% endfor %}
  </ul>
</details>
  {% endunless %}
{% endfor %}







