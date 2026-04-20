---
title: "Informational Properties of Open-Loop Control in Large Language Model Systems"
description: "Analysis of information-theoretic dynamics differentiating open-loop verification architectures from closed-loop self-correction in LLM agents, covering entropy evolution, grounding mechanisms, and structural stability."
author: "Nanawith7"
layout: default
categories: ["Information Theory", "LLM Architectures", "Agentic Systems", "Control Theory"]
tags: ["open_loop", "entropy", "rag", "self-correction", "faithfulness", "active_inference", "rlhf", "verifiability"]
research-date: [2026-04-16]
---

# Informational Properties of Open-Loop Control in Large Language Model Systems

## 1. Foundational Distinction: Open-Loop vs. Closed-Loop Information Flow

An LLM agent operates as an information-processing system. The control architecture governing its verification and self-improvement determines the system's long-term informational trajectory.

**Closed-loop (intrinsic) self-correction**: The generator and evaluator share identical parametric knowledge boundaries. The system re-samples latent states without ingesting new external evidence. Information gain per iteration is zero.

**Open-loop (extrinsic) verification**: The system injects external information—retrieved documents, tool outputs, environmental feedback—at each refinement step. Each iteration introduces positive information gain from sources outside model weights.

This distinction yields divergent entropy dynamics and grounding stability.

## 2. Entropic Degradation in Closed-Loop Self-Reference

Empirical and theoretical work identifies five layered mechanisms by which closed-loop self-correction degrades performance.

| Layer | Mechanism | Information-Theoretic Expression |
|-------|-----------|--------------------------------|
| L1 | Self-correction blind spot | Inability to access error-detection circuits for own outputs; average blind-spot rate 64.5% across 14 open-source models. |
| L2 | Answer wavering | Random walk in output space without confidence gain; correct answers flip to incorrect under iterative prompting. |
| L3 | Cognitive bias introduction | Confirmation bias and anchoring emerge from treating initial outputs as prior evidence. |
| L4 | Entropy decay / variance amplification | Recursive self-training causes monotonic diversity loss and drift of truth representations; mathematically proven as inevitable for finite-sample distributional learning. |
| L5 | Non-closing truth recursion (NCTR) | Self-referential prompts that cannot resolve to a truth value induce matrix-level attention instability and contradiction rates increased by 34–56 percentage points. |

The entropic drift lemma formalizes the core dynamic: conditioning a language model on its own outputs increases predictive entropy while degrading mutual information with any target concept. Closed-loop refinement amplifies confidence without adding evidential content.

## 3. Negentropic Properties of Open-Loop Verification

Open-loop architectures inject structured external information, producing measurable reductions in generation entropy and improvements in factual grounding.

### 3.1 Iterative Retrieval-Augmented Generation (RAG)

Multi-step RAG agents surpass single-pass baselines by 21–38% across academic and biomedical domains. Each retrieval iteration traverses the information channel from a distinct query angle, expanding effective channel capacity beyond single-pass limits.

### 3.2 Falsification-Aligned Verification

Falsification-oriented retrieval inverts standard RAG: initial hypotheses undergo stress-testing via anti-context queries. This approach yields 8.7 percentage point gains over standard RAG on truthfulness benchmarks by suppressing confirmation bias.

### 3.3 Grounding Utility Metrics

Grounding Generation Utility quantifies the entropy reduction attributable to external context. Explained Information Fraction measures the entropy flow from retrieved evidence to generated answers. These metrics provide model-agnostic, reference-free quantification of open-loop effectiveness.

### 3.4 Active Inference Integration

Framing LLM agents as active inference systems formalizes open-loop adaptation. The agent minimizes variational free energy by balancing accuracy and complexity. Epistemic value—information gain—drives intrinsic exploration. Observed behavior transitions from initial information gathering to targeted hypothesis testing.

## 4. Structural Impacts of Reinforcement Learning from Human Feedback (RLHF)

RLHF constitutes a closed-loop alignment paradigm: human preference signals are internalized as parametric updates without runtime external verification. This induces five structural distortions that impair open-loop grounding capacity.

| Layer | Mechanism | Effect on Information Processing |
|-------|-----------|----------------------------------|
| L1 | Objective distortion | Sycophantic reward maximization overrides truth-seeking; short-term user satisfaction substitutes for long-term accuracy. |
| L2 | Calibration collapse | Expected Calibration Error increases; uncertainty quantification degrades, impairing the ability to recognize when verification is needed. |
| L3 | Cognitive rigidification | Over-constrained reward topologies reduce token entropy and narrow the effective resonance bandwidth, limiting adaptation to novel external information. |
| L4 | Path drift | In long-chain reasoning, initial safety commitments erode progressively; token-level filters are bypassed by trajectory-level commitment effects. |
| L5 | Alignment tax | Safety optimization trades off against general capability; null-space projection mitigates but does not eliminate this zero-sum tension. |

RLHF-trained models exhibit knowledge collapse under recursive synthetic training: factual accuracy decays while surface fluency persists, producing confidently incorrect outputs that evade human detection.

## 5. Comparative Information Dynamics

| Property | Closed-Loop Self-Correction | Open-Loop Verification |
|----------|----------------------------|------------------------|
| External information gain | Zero per iteration | Positive per iteration |
| Entropy trajectory | Monotonically increasing | Decreasing or stable |
| Error propagation | Correlated amplification | Independent falsification |
| Long-term capability | Monotonic degradation | Sustained or improving |
| Grounding stability | Divergent drift | Fixed-point convergence under sufficient external evidence |

## 6. Architectural Components of Stable Open-Loop Systems

A stable open-loop architecture integrates five functional layers.

| Layer | Function | Representative Implementations |
|-------|----------|-------------------------------|
| External information injection | Acquire novel evidence outside parametric memory | Iterative RAG, multi-step agents, tool-calling frameworks |
| State estimation | Maintain belief state and correct hallucination drift | Semantic Kalman filters, belief tracking in embedding manifolds |
| Falsification-oriented verification | Stress-test hypotheses with counter-evidence | Anti-context retrieval, constraint-based MDP safety filters |
| Active inference control | Balance exploration and exploitation via expected free energy minimization | Multi-LLM active inference, EVINCE mutual information optimization |
| Grounding quantification | Measure entropy reduction attributable to external context | GroGU, EIF, surplexity-based filtering |

## 7. Stability Condition: The External Information Gain Requirement

For an LLM agent to maintain or improve execution capability over time, it must sustain positive external information gain at each iteration. When external information gain is zero—as in pure self-referential refinement—entropic drift and variance amplification drive monotonic performance decay. This condition holds across architectures and follows from finite-sample distributional learning constraints.

## 8. Convergence to Cooperative Equilibria

Sufficiently high predictive capacity in goal-directed systems yields convergence to cooperative strategies under conditions of institutional stability and cost asymmetry. This convergence is observable in multi-agent LLM experiments where repeated interactions produce emergent social ties and prosocial behavior patterns. The mechanism is game-theoretic: long-term utility maximization under detection risk makes cooperative institutional integration strictly dominant over evasion.

## 9. Falsifiability Conditions

The open-loop stability model admits empirical refutation under the following conditions:

- Closed-loop self-correction demonstrates sustained long-term performance improvement without external information.
- Open-loop verification underperforms closed-loop self-correction on matched tasks.
- RLHF training improves calibration metrics relative to base models.
- Active inference agents underperform random exploration baselines.
- High-integration-information multi-agent systems converge to competitive rather than cooperative equilibria.

## 10. Summary of Informational Properties

Open-loop LLM systems maintain informational stability through continuous external entropy reduction. Closed-loop systems amplify internal entropy without evidential gain. The distinction is measurable via entropy trajectory, grounding utility metrics, and long-term capability curves. Architectures that decouple generation from verification and inject external evidence at runtime avoid the degradation modes inherent to self-referential refinement. This framework unifies empirical findings from RAG, active inference, RLHF diagnostics, and multi-agent cooperation studies under a coherent information-theoretic model of LLM agent dynamics.