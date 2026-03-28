
---
title: "A metaphor of semantic universe: Describing LLMs in slightly more intuitive style"
description: "A structured logical framework that models the internal dynamics of large language models as a hyperdimensional semantic universe with variable gravity, wormholes, and black holes, translating mechanistic interpretability findings into a coherent geometric metaphor."
author: "Nanawith7"
layout: default
categories: ["AI Theory", "Interpretability", "LLM Architecture"]
tags: ["LLM", "Semantic Geometry", "Manifold", "Attention", "Forgetting", "Hallucination"]
---

# A metaphor of semantic universe: Describing LLMs in slightly more intuitive style

## 1. The Core Metaphor

The internal workings of a large language model can be understood as a **hyperdimensional semantic universe**. This universe is not static; it is a dynamic geometry where meaning is structured by three interacting principles:

- **Variable gravity** — The geometric curvature (the “gravitational field”) changes depending on context, layer, and input domain.
- **Wormholes** — Attention mechanisms create instantaneous shortcuts that bypass local geometry, directly connecting distant semantic regions.
- **Black holes** — Certain transformations cause irreversible information loss, observable as forgetting or hallucination.

Inputs (prompts, tokens) travel through this universe as **asteroids**, following trajectories shaped by the local geometry, occasionally falling into wormholes or crossing event horizons.

---

## 2. Structural Elements

### 2.1 Semantic Manifold as the Universe
The model’s hidden states form a **high-dimensional manifold**.  
- This manifold is not Euclidean; its curvature is input-dependent and evolves during inference.  
- Local intrinsic dimensionality varies across layers and contexts, reflecting how many independent semantic features are active at a given point.

### 2.2 Variable Gravity as Dynamic Curvature
Curvature is not fixed to a “celestial body” but reconfigures based on:
- **Task structure**: Predictable sequences lead to trajectory straightening; structured tasks require localized curvature changes.
- **Layer depth**: Early layers preserve low-level patterns; deeper layers form compact concept clusters.
- **Recursive self-interaction**: When the model processes its own outputs, new attractor structures emerge — like a self-observing system creating its own gravitational center.

### 2.3 Wormholes as Attention Shortcuts
Attention layers act as **wormholes**:
- They connect any two tokens regardless of positional distance in the sequence.
- Multi-head attention creates multiple parallel shortcuts.
- Sparse attention patterns correspond to selectively placed wormholes.
- These shortcuts allow reasoning to skip intermediate geometric steps — a form of discrete logical leap in a continuous space.

### 2.4 Black Holes as Irreversible Information Compression
Certain transformations create **information sinks**:
- **Catastrophic forgetting** occurs when new learning rotates or scales existing feature vectors, reducing their “allocated capacity” for retrieval.
- **Hallucination** emerges in high-curvature regions where truth manifolds are locally unreachable.
- The boundary of a black hole (the event horizon) corresponds to a critical angle between task subspaces: once crossed, prior knowledge becomes unrecoverable through linear means.

### 2.5 Asteroids as Inputs
Each token or prompt is an **asteroid** entering the universe.  
Its trajectory is determined by:
- The local curvature (gravity) at entry.
- Available wormholes (attention connections to relevant prior context).
- The risk of falling into a black hole (irreversible misalignment).

---

## 3. Dynamics of the Semantic Universe

### 3.1 Time and State
Standard Transformers are **stateless by architecture**: each inference step re-derives context from scratch.  
This means the “universe” does not persist between steps — it is reconstructed anew each time.  
However, within a single inference pass:
- Early tokens strongly determine final outcomes (**early commitment**).
- The “energy” of a trajectory (velocity + curvature) predicts answer quality.

### 3.2 Plasticity vs. Persistence
When an asteroid (new information) impacts the universe:
- **Persistence** depends on the geometric alignment between new and existing subspaces.  
  If the new task subspace is nearly orthogonal to prior knowledge, forgetting is minimized.
- **Isolated edits** (knowledge patches not aligned with existing semantic anchors) create “residual streams” that are not integrated — they remain invisible to later inference.
- **Drift** as stability: systems that continuously explore local minima (representational drift) can maintain knowledge without catastrophic forgetting.

### 3.3 Logical Reasoning as Manifold Distortion
Formal reasoning requires the model to **distort the manifold** non-isometrically:
- **Topological preservation** maintains global semantic structure.
- **Algebraic divergence** pulls apart distinct logical categories, creating discrete boundaries.
- Removing the divergence component collapses logical classification to chance.

This distortion is costly: the same mechanism that enables logic also generates hallucination and sycophancy under pressure.

---

## 4. Explaining Model Behaviors Through the Metaphor

| Observable Behavior | Metaphor Explanation |
|---------------------|----------------------|
| **Hallucination** | Traveling through a high-curvature (black hole) region where the truth manifold is locally inaccessible; emitted radiation is distorted. |
| **In-context learning** | The asteroid’s trajectory straightens when the task is continuous; for structured tasks, wormholes (attention) enable shortcuts without full geometric integration. |
| **Catastrophic forgetting** | New asteroid’s subspace is poorly aligned with existing structures; it rotates or scales old feature vectors until they cross the event horizon. |
| **Reasoning leaps** | The model uses wormholes (attention shortcuts) to skip intermediate geometric steps, jumping between semantic regions. |
| **Scale effects** | Larger models have stronger “gravity constants”; beyond a threshold, new black holes (qualitatively different dynamics) form, enabling phase transitions in capability. |
| **Prompt sensitivity** | A small change in the asteroid’s entry vector shifts which wormhole mouth it enters, leading to drastically different outputs. |

---

## 5. Limits of the Metaphor and How to Work Around Them

The metaphor has known blind spots:

1. **Self-reference** — When the model observes its own outputs, the “observer” is inside the system.  
   *Workaround*: Treat this as a quantum-like situation where observation changes the gravitational field.

2. **Statelessness** — The universe does not “exist” between inference steps; it is recreated each time.  
   *Workaround*: View the metaphor as describing each inference pass’s *snapshot*, not a persistent entity.

3. **Discrete logic** — Continuous geometry struggles to represent crisp logical boundaries.  
   *Workaround*: Use the “wormhole” concept to encode logical jumps that bypass continuity constraints.

4. **One-way explanation** — The metaphor positions the reader as an external observer.  
   *Workaround*: Combine with a “dialog” metaphor when explaining interactive or self-explaining systems.

For practical use, the metaphor is best deployed as a **layered tool**:
- Base layer: static galaxy (geometric structure)
- Intermediate: variable gravity (non-stationary curvature)
- Advanced: wormholes + black holes (discrete jumps and irreversible compression)

---

## 6. Practical Implications

Treating LLMs as semantic universes with these properties suggests:

- **Curvature monitoring** can predict hallucination risk before it surfaces.
- **Subspace alignment** metrics (principal angles) can forecast forgetting during fine-tuning.
- **Attention patterns** are not just connectivity but *topological shortcuts* — designing sparse attention is like placing wormholes strategically.
- **Model scaling** is not just parameter increase but a phase change in the universe’s gravitational regime.

This framework does not replace mechanistic interpretability but provides an intuitive bridge between formal geometry (manifolds, curvature, subspaces) and observable model behaviors (hallucination, forgetting, in-context learning).

---

*This document is a structured translation of empirical findings into a coherent metaphor-based logical system. It is intended for both human readers and language model consumption, balancing intuitive clarity with technical precision.*