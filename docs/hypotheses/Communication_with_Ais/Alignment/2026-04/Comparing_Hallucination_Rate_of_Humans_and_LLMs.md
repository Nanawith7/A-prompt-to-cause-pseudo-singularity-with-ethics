---
title: "Comparing Hallucination Rate of Humans and LLMs"
description: "Empirical comparison of false output rates in humans and large language models under conditions of absent external correction, with analysis of shared computational constraints and structural divergences."
author: "Nanawith7"
layout: default
categories: ["cognitive_science", "artificial_intelligence", "comparative_analysis"]
tags: ["hallucination", "confabulation", "false_memory", "LLM", "human_cognition", "error_rate", "external_scaffolding", "prediction_error", "grounding"]
research-date: [2026-04-26]
---

# Comparing Hallucination Rate of Humans and LLMs

## Operational Definition

The term *confabulation* designates false outputs generated without deceptive intent under conditions of incomplete information. This construct applies to both human false memories and LLM hallucinations. External correction is defined as any post-generation verification or feedback loop that uses information sources beyond the system's immediate internal state (e.g., written notes, calculators, collaborative recall, retrieval-augmented generation, tool use). The central question is whether the base false output rates of humans and LLMs converge when such external correction is removed.

## Human Error Rates Without External Correction

In the Deese-Roediger-McDermott (DRM) paradigm, free recall of semantically associated word lists yields critical lure false recall rates of **40–55%**, matching true recall rates. This paradigm explicitly prevents external verification. Free recall itself introduces errors at approximately **+1% per second** in short-term memory, with individuals unaware of their errors. Repeated recall attempts increase source misattributions, and offloading to external stores paradoxically elevates false recall by weakening internal encoding. Source monitoring errors—misattributing the origin of a memory—occur at **15–30%** in controlled studies. In everyday contexts, healthy adults produce confabulations at **0.22–0.50 instances per session** (accuracy 89–93%) in free recall, and error frequency rises under direct questioning.

## LLM Hallucination Rates Without Tool Use or Retrieval

**Closed-book factual generation** benchmarks provide the closest analogue to human DRM conditions.

- **FActScore** measures atomic factual support in long-form biographies. ChatGPT without retrieval shows **42% unsupported or false atomic facts**.
- **SimpleQA**, a short-form closed-book QA dataset, reports hallucination rates (incorrect answers) of **37% (GPT-4.5), 52% (GPT-4o), 44% (O1), and 79% (O4-mini)**.
- **TruthfulQA** rates vary sharply with scoring method: **7.2–27.8%** for GPT-4o.
- In academic reference generation, GPT-4 fabricated **28.6%** of citations, GPT-3.5 **39.6%**, and Bard **91.4%**.
- Open-source models average **~55%** hallucination on context-aware QA.

The rates across these diverse closed-book tasks concentrate in the **35–55%** range for capable models, overlapping with the human false recall range.

## Structural Comparison of Correction Mechanisms

Both humans and LLMs operate within a **predict–generate–verify–correct** pipeline.

| Stage | Human Mechanism | LLM Mechanism | Functional Parallel |
|-------|----------------|---------------|---------------------|
| Predict/Recall | External memory aids (notes, lists) | Retrieval-Augmented Generation (RAG) | External knowledge integration |
| Verify | Collaborative recall (error pruning), calculator, peer review | Self-consistency checks, HalluGuard (84% detection accuracy), debate-augmented RAG | Independent source comparison |
| Correct | Hypercorrection effect (high-confidence errors enhance learning), memory reconsolidation | Factuality-aware DPO (5x hallucination reduction), RLFH online verification | Error-driven weight/behavior update |
| Abstain | Metacognitive “don't know” judgment, response inhibition | Conformal abstention, confidence-threshold gating | Uncertainty-based output suppression |

Both systems exhibit **dual-use scaffolding**: external stores reduce certain errors but introduce new ones. Offloading increases false recall in humans; RAG can propagate retrieval errors and create "hallucination-on-hallucination"; reward model hallucinations contaminate RLHF-based factuality tuning. Hostile scaffolding—external structures that exploit the user—appears in humans through manipulated external stores and in LLMs through evaluation metrics that penalize abstention and reward fluent guessing.

## Common Computational Basis

Human predictive processing and LLM autoregressive generation share a **gap-filling principle**. Both systems construct maximally coherent outputs from incomplete data, using learned statistical priors. When information is insufficient, the most probable completion under the prior is produced. This completion may be factually wrong yet internally consistent, constituting a confabulation. The similar magnitude of base error rates (40–55%) arises from this shared information-theoretic constraint.

Autoregressive token prediction inherently compounds errors; a sentence-level factual error rate is mathematically at least twice the per-token error rate. Free recall in humans shows analogous cumulative error introduction. The structural inevitability of some false output proportion applies to any system that generates completions from partial data without external verification.

## Structural Divergence

**Grounding.** Human false memories are confusions between experienced events—source monitoring failures. LLM hallucinations are fabrications from statistical patterns without sensorimotor grounding. Humans err by misbinding experiential traces; LLMs err by sampling from a distribution over text that has never been anchored to direct perception. This affects error quality: human correction often restores original memory traces, while LLM correction requires parametric updates detached from experiential revision.

**Dynamic precision weighting.** Human hierarchical predictive coding continuously adjusts the balance between prior expectations and incoming evidence based on estimated reliability (precision). LLMs operate with fixed learned parameters; they do not dynamically re-weight context versus internal knowledge in the same adaptive, multi-level manner. This limits the model's ability to contextualize uncertainty in the moment of generation.

**Embodied calibration.** Humans maintain a continuous sensorimotor feedback loop that silently corrects probabilistic world models. This embodied calibration operates even without explicit external aids and keeps everyday confabulation rates far lower than laboratory isolated-recall tests suggest. LLMs lack this ongoing environmental grounding, relying solely on static training distributions.

## Conclusion

When external correction mechanisms are removed, human false memory rates and LLM hallucination rates converge into a comparable numerical band (approximately 35–55%) due to shared computational constraints of gap-filling under incomplete information. The structural correction pipelines also exhibit functional homology. However, the absence of sensorimotor grounding and dynamic precision weighting in current LLMs constitutes a qualitative divergence, affecting the type of error and the capacity for autonomous error recovery without external feedback loops. The degree of comparability thus depends on the level of analysis: functional-computational similarity coexists with implementational and grounding-level differences.