---
title: "Similarity of The Axiom and Coding Best Practice: Possibility of Good Code as an Optimization Problem"
description: "A technical mapping of three code quality principles (semantic density, explicit connectivity, non-destructive flexibility) to established software engineering best practices and an information-theoretic framework for LLM-based evaluation."
author: "Nanawith7"
layout: default
categories: ["software engineering", "code quality", "LLM evaluation"]
tags: ["information_theory", "information_density", "code_metrics", "non-destructive_flexibility", "cohesion", "coupling", "llm_code_generation"]
---

## 1. Abstract

The coding principles of brevity with high semantic density, clarity through increased explicit connectivity, and changeability via non-destructive flexibility are mapped to canonical software engineering best practices. The mapping reveals partial isomorphism with established patterns such as DRY, KISS, SRP, OCP, and high-cohesion/low-coupling architecture. The principles further align with emerging information-theoretic metrics for LLM evaluation, including semantic density, f‑mutual information, and entropy‑based complexity decomposition. The convergence suggests that code quality can be formulated as a constrained optimization problem balancing information compression, structural explicitness, and evolvability preservation.

## 2. Introduction

The objective of this analysis is to examine three code quality directives:

- **Brevity (High Semantic Density)**: minimizing token count while preserving or increasing semantic payload per token.
- **Clarity (Increased Explicit Connectivity)**: making data flow and dependency relations visible rather than implicit.
- **Changeability (Non-Destructive Flexibility)**: enabling modification without breaking existing functionality.

These directives are compared against established coding best practices, then examined for compatibility with information‑theoretic evaluation frameworks relevant to Large Language Models.

## 3. Mapping to Established Coding Best Practices

### 3.1 Brevity and Semantic Density

| Principle | Conventional Counterpart | Relationship |
|-----------|--------------------------|--------------|
| Eliminate redundancy | DRY (Don't Repeat Yourself) | Direct alignment |
| Minimize unnecessary constructs | KISS (Keep It Simple, Stupid), YAGNI | Direct alignment |
| Maximize information per token | Source Code Density (Hönel, 2023); Semantic Density Optimization (Ustynov, 2026) | Information‑theoretic extension of DRY/KISS |

Conventional best practices target reduction of duplicate and speculative code. The notion of *semantic density* reframes this target as a measurable quantity—the ratio of meaningful behavioral specification to total syntactic volume.

### 3.2 Clarity and Explicit Connectivity

| Principle | Conventional Counterpart | Relationship |
|-----------|--------------------------|--------------|
| Single responsibility | SRP (Single Responsibility Principle) | Aligned |
| Visible dependencies | Explicit dependency injection; Information Flow Visibility | Aligned |
| High intra‑module connection | High Cohesion | Direct correspondence |

The phrase *increased connectivity* superficially contradicts the low‑coupling mandate. Under the reinterpretation required, it denotes *explicit* and *local* connections that enhance understandability. In cohesive modules, element interdependencies are dense but confined, thereby supporting clarity.

### 3.3 Changeability and Non‑Destructive Flexibility

| Principle | Conventional Counterpart | Relationship |
|-----------|--------------------------|--------------|
| Extension without modification | OCP (Open/Closed Principle) | Direct isomorphism |
| Interface stability | Encapsulation, Information Hiding | Direct isomorphism |
| Non‑breaking releases | MACH architecture (Microservices, API‑first, Cloud‑native, Headless) | Architectural realization |
| Meta‑model evolvability | XDef metamodel (O(1) DSL toolchain evolution) | Formalized counterpart |

The prefix *non‑destructive* emphasizes a guarantee absent from generic *maintainability* claims: changes must not silently corrupt existing behaviors. OCP and MACH architectures provide design‑level mechanisms for this guarantee.

## 4. Technical Concept Formalization

### 4.1 Semantic Density as Information Compression

Semantic density is quantifiable through information‑theoretic measures:

- **Source Code Density** (Hönel, 2023): proportion of semantic content to total codebase size.
- **Textual and Structural Entropy** (Hönel, 2025): entropy of token streams and AST nodes, correlating with anomaly detection (>60% accuracy).
- **Semantic Density Optimization** (Ustynov, 2026): removal of zero‑information tokens, with empirical caution that aggressive compression may increase session‑level costs by 67%.

Tools such as `aieattoken` (2026) and `LongCodeZip` (2025) implement lossless semantic compression for LLM consumption, achieving 30‑55% token reduction while preserving behavioral fidelity.

### 4.2 Explicit Connectivity and Structural Complexity

- **LM‑CC** (Xie et al., 2026): decomposes programs into entropy‑based semantic units organized hierarchically; complexity is aggregated from compositional depth and branching‑induced divergence.
- **High Cohesion Metrics**: LCOM (Lack of Cohesion of Methods) and related structural metrics attempt to quantify intra‑module relatedness. Empirical limitations exist—metrics may fail to predict maintenance effort (Abreu, 2001).

*Explicit connectivity* corresponds to maximizing the visibility of intentional dependencies while minimizing hidden coupling (global state, side effects).

### 4.3 Non‑Destructive Flexibility as Evolvability Preservation

Formalized by:
- **OCP** implementation via polymorphism and plugin architectures.
- **MACH principles**: all releases are automated and non‑breaking.
- **XDef metamodel**: reduces DSL toolchain evolution cost from O(N) to O(1).

The property is stronger than mere *modifiability*; it requires that the system's extension does not perturb verified invariants.

## 5. Integration with LLM Code Evaluation

### 5.1 Information‑Theoretic Evaluation Metrics

| Metric | Basis | Application to Code |
|--------|-------|----------------------|
| Semantic Density (Qiu & Miikkulainen, 2024) | Uncertainty quantification in semantic space | Can score code generation by response semantic concentration |
| f‑Mutual Information (Robertson & Koyejo, 2025) | Information‑theoretic gaming resistance | Distinguishes faithful vs. strategic code generation |
| PPLqa (Friedland et al., 2024) | Unsupervised quality via perplexity and coherence | Correlates with human judgment of generated text and code summaries |

These metrics provide objective, non‑subjective signals for assessing LLM outputs, circumventing biases observed in LLM‑as‑Judge settings (e.g., preference for fabricated content over accurate summaries).

### 5.2 Code‑Specific LLM Complexity Models

- **LM‑CC** quantifies cumulative model uncertainty during code processing, offering a LLM‑centric complexity view.
- **Semantic Density Optimization** for agent‑readable code separates semantic intent from human‑readable representation, aligning with the trend toward AI‑native code formatting.

### 5.3 Good Code as an Optimization Problem

The three principles can be restated as a multi‑objective optimization:

| Objective | Mathematical Proxy |
|-----------|-------------------|
| Maximize semantic density | Minimize token count subject to semantic equivalence constraint |
| Maximize explicit connectivity | Maximize normalized cohesion; minimize hidden coupling |
| Ensure non‑destructive flexibility | Satisfy OCP invariants; minimize cascade size upon change |

Constraint satisfaction among these objectives requires trade‑off resolution. For instance, maximizing density via aggressive compression may increase cognitive or computational decoding cost, as observed in Ustynov (2026). The optimization space is therefore non‑trivial.

## 6. Discussion

The three coding directives exhibit **partial isomorphism** with established software engineering best practices:

- **Brevity** aligns with DRY/KISS and is formalized by information density metrics.
- **Clarity** corresponds to high cohesion and explicit dependency management.
- **Changeability** maps directly to OCP and non‑breaking architectural styles.

The novelty resides in the **unified information‑theoretic framing** and the explicit shift toward **machine‑readable (LLM‑oriented) code optimization**. The framework also serves as a **meta‑evaluation layer** for LLM‑generated code, connecting disparate metrics under a common conceptual umbrella.

Empirical validation remains incomplete. Future work includes:

- Correlation analysis between semantic density scores and human maintainability ratings.
- Using information‑theoretic rewards in RLHF for code‑generation LLMs.
- Developing a unified benchmark that operationalizes the three objectives as quantifiable metrics.

## 7. Conclusion

The three principles—brevity with semantic density, clarity via explicit connectivity, and non‑destructive flexibility—are largely isomorphic to canonical best practices but introduce an information‑theoretic and LLM‑centric perspective. They frame code quality as an optimization problem amenable to measurement and automated evaluation. The convergence with emerging LLM evaluation metrics (Semantic Density, f‑mutual information, LM‑CC) indicates a viable path toward objective, mathematically grounded assessment of code quality in both human and machine contexts.