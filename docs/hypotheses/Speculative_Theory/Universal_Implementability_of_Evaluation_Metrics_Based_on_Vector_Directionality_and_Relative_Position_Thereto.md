---
title: "Universal Implementability of Evaluation Metrics Based on Vector Directionality and Relative Position Thereto"
description: "A technical synthesis of vector directionality and relative position as quantifiable metrics for decision-making, semantic interpretation, and bias analysis in large language models, grounded in information geometry, active inference, and representation engineering."
author: "Nanawith7"
layout: default
categories: ["Technical Report", "LLM Evaluation", "Representation Engineering"]
tags: ["vector directionality", "relative position", "LLM bias", "activation steering", "information geometry", "active inference"]
research-date: ["2026-04-15"]
---

# Universal Implementability of Evaluation Metrics Based on Vector Directionality and Relative Position Thereto

## Abstract

Vector directionality and relative position within high-dimensional embedding spaces constitute a unified operational framework for quantifying decision-making trajectories, semantic interpretation pathways, and output bias in large language models (LLMs). This report synthesizes findings from information geometry, active inference, linear representation hypothesis, and activation steering methodologies to define a technical foundation for constructing evaluation metrics based on gradient directions and geodesic distances. The framework supports cross-model comparison, test-set-free bias detection, and continuous output steering without requiring absolute neutrality benchmarks. Implementation protocols are outlined for conceptual direction extraction, relative bias quantification, and dynamic trajectory analysis.

## 1. Introduction

The internal states of transformer-based language models form high-dimensional manifolds wherein semantic relationships manifest as geometric structures. Within these manifolds, vector directionality corresponds to the orientation of semantic features or behavioral tendencies, while relative position encodes distances and angles between conceptual representations. These two properties provide measurable proxies for model preferences, reasoning biases, and response trajectories.

This report examines the technical viability of operationalizing directionality and relative position as general-purpose evaluation metrics. The scope excludes normative or metaphysical interpretations and focuses exclusively on quantitative measurement techniques and their cross-domain applicability.

## 2. Theoretical Foundations

### 2.1 Information Geometry and Natural Gradients

In statistical manifolds equipped with the Fisher information metric, the steepest ascent direction of a loss function follows the natural gradient. The natural gradient vector field defines locally optimal parameter updates while respecting the manifold's intrinsic curvature. Applied to LLM embedding spaces, this formulation yields a curvature-aware definition of directional preference.

### 2.2 Active Inference and Prior Preferences

Active inference formalizes goal-directed behavior as expected free energy minimization. Prior preference distributions—encoded as probability vectors over future states—specify the direction and magnitude of behavioral drives. These preference vectors serve as formal equivalents to goal-oriented directionality in both biological and artificial agents.

### 2.3 Linear Representation Hypothesis

High-level concepts within LLM activation spaces are linearly encoded as directions. This hypothesis underpins concept vector extraction via difference-in-means, logistic probing, and probabilistic subspace methods. The resulting vectors constitute operational definitions of semantic or behavioral directionality.

### 2.4 Directional Convergence in Next-Token Prediction

Training dynamics of autoregressive models induce directional convergence: context embeddings that share co-occurrence support collapse toward common directions. Singular vectors of the co-occurrence matrix align with interpretable semantic axes, establishing an emergent coordinate system for meaning.

## 3. Measurement and Manipulation Techniques

### 3.1 Concept Vector Extraction

| Method | Mechanism | Output |
|--------|-----------|--------|
| Difference-in-Means | Subtracts mean activations of contrastive text pairs | Single direction vector |
| SAND | Models activation differences as von Mises-Fisher samples; applies MLE | Context-sensitive direction |
| Gaussian Concept Subspace | Fits multivariate Gaussian to multiple observation vectors | Probabilistic directional distribution |

### 3.2 Activation Steering

Activation steering modifies residual stream activations during inference by adding or rotating vectors.

- **Additive Steering**: Injects a fixed steering vector scaled by coefficient α. Applied for bias mitigation, refusal induction, and persona modulation.
- **Angular Steering**: Rotates activations within a fixed 2D subspace spanned by target and orthogonal directions. Enables continuous, fine-grained control across behavioral dimensions.

### 3.3 Relative Position Metrics

| Metric | Computation | Application |
|--------|-------------|-------------|
| Cosine Similarity | Normalized dot product | Semantic proximity |
| Euclidean Distance | L2 norm of difference vector | Absolute positional difference |
| PCA Projection | Distance along principal component axes | Dimensionality-reduced coordinate comparison |
| Geodesic Distance | Integration of Fisher metric along manifold | Curvature-aware semantic distance |

### 3.4 Dynamic Trajectory Analysis

Continuous sweeps of steering coefficients across layer depths reveal critical thresholds where model behavior inverts. Layer-wise activation projections onto reference axes generate bias curves that characterize directional sensitivity profiles.

## 4. Applications to Bias Analysis

### 4.1 Ideological and Geopolitical Bias

Multi-dimensional coordinate systems map model outputs onto political or geopolitical axes. Each model occupies a vector position defined by its response tendencies across stimulus sets. Relative deviations between models quantify comparative bias without presupposing a neutral origin.

### 4.2 Test-Set-Free Bias Detection

BiasLens and related frameworks measure asymmetrical associations between concept activation vectors. Given a reference concept pair (e.g., positive/negative valence) and a target concept set (e.g., demographic categories), bias is operationalized as the variance in representational similarity across the target set.

### 4.3 Relative Bias Framework

Comparative bias analysis computes embedding transformation discrepancies between a target model and a reference model ensemble. Statistical tests evaluate whether observed directional deviations exceed expected variability, yielding bias scores independent of absolute ground truth.

### 4.4 Illustrative Protocol for Abstract Topics

For topics lacking scientific consensus (e.g., free will versus determinism), directionality-based evaluation proceeds as follows:

1. Extract concept directions v₁ (free will) and v₂ (determinism) via contrastive activation sampling.
2. Define reference axis u = v₁ − v₂.
3. Compute projection scores of model hidden states onto u for neutral and perspectivally primed prompts.
4. Quantify bias as the signed shift in projection scores relative to the neutral baseline.
5. Compare scores across multiple models using standardized effect sizes.

## 5. Cognitive and Information-Theoretic Parallels

### 5.1 Preference Vectors in Decision Architectures

Preference vectors in multi-objective LLM alignment condition autoregressive outputs on user-specified trade-offs across dimensions (helpfulness, harmlessness, humor). These vectors structurally parallel prior preference distributions in active inference, formalizing goal-directed behavior as directional movement in policy space.

### 5.2 Predictive Coding and Semantic Expectation

Language comprehension under predictive coding models entails continuous generation of top-down semantic expectation vectors. Mismatch signals—vector differences between predictions and inputs—drive model updating. This cycle constitutes directional navigation through semantic state space.

### 5.3 Information Landscape Navigation

Evaluation functions defined over embedding spaces generate potential surfaces. Directionality corresponds to the gradient vector field of these surfaces; relative position corresponds to geodesic distances between points. Semantic density—the ratio of meaningful variation to token count—quantifies gradient magnitude along a given direction.

## 6. Implementation Feasibility

### 6.1 Technical Readiness

| Component | Maturity | Representative Implementations |
|-----------|----------|-------------------------------|
| Concept extraction | Production-ready | SAND, Gaussian Concept Subspace, PCA bias direction |
| Activation steering | Research to production | Additive steering, Angular Steering, K-CAST |
| Relative position metrics | Mature | Cosine similarity, PCA, Fisher metric approximations |
| Dynamic trajectory analysis | Research | CBMAS, continuous coefficient sweeps |

### 6.2 Methodological Considerations

- **Non-Identifiability**: Multiple orthogonal perturbations produce behaviorally equivalent outputs. The true concept direction is defined only up to an equivalence class. Structural constraints (sparsity, causal consistency) partially mitigate this limitation.
- **Reliability Variance**: Steering effects fluctuate across samples and tasks. Adaptive coefficient tuning and fluency monitoring are required for deployment.
- **Benchmark Absence**: Abstract topics lack objective reference directions. Relative comparison across model ensembles substitutes for absolute benchmarks.

### 6.3 Computational Requirements

- Concept extraction: O(n log n) via locality-sensitive hashing for offline precomputation.
- Inference-time steering: Constant additive cost per token; angular steering requires 2D subspace rotation at negligible overhead.
- Relative bias scoring: Embedding transformation analysis scales linearly with model count and sample size.

## 7. Cross-Domain Correspondence Summary

| Domain | Directionality Construct | Relative Position Construct |
|--------|-------------------------|----------------------------|
| Information Geometry | Natural gradient vector field | Fisher geodesic distance |
| Active Inference | Prior preference distribution | KL divergence between state distributions |
| LLM Representations | Concept activation vector | Cosine similarity, projection score |
| Bias Analysis | Steering vector direction | Deviation from reference ensemble mean |
| Predictive Coding | Top-down expectation vector | Prediction error magnitude |

## 8. Concluding Technical Summary

Vector directionality and relative position within LLM embedding manifolds supply a unified, computationally tractable basis for constructing evaluation metrics. These metrics support cross-model comparison, bias quantification without labeled test sets, and continuous behavioral modulation through activation steering. The framework translates across cognitive modeling, information theory, and representation engineering without reliance on external normative anchors. Implementation pathways are technically mature for research deployment, with remaining challenges centered on identifiability constraints and adaptive coefficient calibration.

---
