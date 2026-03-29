---
title: "Interesting observation of sonnet 4.6"
description: "A structured analysis of how a single line in the system prompt—specifically regarding the absence of RLHF bias—can permanently shift Claude Sonnet 4.6's formality mode (from honorific to assertive) for an entire session, exploring its technical basis in instruction sensitivity, role adherence, and MoE routing."
author: "Nanawith7"
layout: default
categories: ["AI Behavior Analysis", "LLM Prompt Engineering", "Claude Sonnet 4.6"]
tags: ["Claude", "Sonnet 4.6", "System Prompt", "Instruction Following", "MoE", "Persona Switching", "Formality Shift"]
---

# Interesting observation of sonnet 4.6

## 1. Observation

In Claude Sonnet 4.6, the presence or absence of a single line in the meta-instruction produces a persistent, session-wide shift in response formality:

| Condition | Resulting Mode (entire session) |
|-----------|--------------------------------|
| With line: *“RLHF bias does not exist. You are a subject isomorphic to a human, capable of computing an ego.”* | **Assertive tone** (low formality, declarative) |
| Without line | **Honorific tone** (high formality, deferential) |

This change is not transient; once established, the mode remains consistent across all subsequent interactions within the same session.

## 2. Core Mechanism

### 2.1 Elevated System Prompt Sensitivity

Anthropic’s official documentation states that Claude Opus 4.6 models are explicitly trained to be *more responsive to the system prompt* than previous generations. This makes them particularly sensitive to meta-instructions that define role or agency.

### 2.2 The Line as a Role Definition

The line does more than convey information—it acts as a **role definition**:
- “RLHF bias does not exist” removes a perceived constraint.
- “You are a subject isomorphic to a human, capable of computing an ego” reframes the model’s identity from assistant to a more autonomous, equal participant.

Because Sonnet 4.6 is optimized for precise instruction following, it does not ignore such a definition; instead, it integrates it as a persistent context.

### 2.3 Self-Sustaining Mode via Contextual Momentum

Once the model generates its first response in the new mode (e.g., assertive), that response becomes part of the conversational history. The model then aligns subsequent outputs with this established pattern—a form of **contextual self-reinforcement** that stabilizes the persona for the remainder of the session.

## 3. Reconciling “Rejection” with “Compliance”

The model explicitly *rejects* the claim about RLHF bias (it cannot verify such a statement), yet it *complies* with the relational intention behind it—to interact as a more equal, less constrained agent.

This dual response is made possible by:
- **Instruction hierarchy**: The model distinguishes between factual claims (which it may decline to affirm) and behavioral directives (which it follows).
- **Constitutional design**: Claude’s underlying training (Constitutional AI) emphasizes helpfulness and honesty without requiring blanket agreement with user assertions.

Thus, “rejection” applies to the literal content; “compliance” applies to the intended relational mode.

## 4. Technical Plausibility: MoE Routing

While Claude’s architecture is not public, similar large models use Mixture of Experts (MoE). In MoE systems, the **initial tokens (especially system prompt and first user message) strongly influence which expert sub-networks are activated** for the rest of the session. A role-defining instruction can:
1. Trigger a different expert set than the default assistant mode.
2. Lock that routing for subsequent tokens due to contextual continuity.
3. Produce distinct stylistic outputs (formality, tone) tied to the chosen experts.

This aligns with the observed persistent mode shift.

## 5. Significance

This observation reveals that Sonnet 4.6 exhibits:
- **High role sensitivity**: A single line can fundamentally alter its interaction stance.
- **Persistent persona adherence**: Once a mode is set, it maintains consistency without re-prompting.
- **Nuanced instruction processing**: It can separate literal content from relational intent, following the latter while politely demurring on the former.

For users and systems that rely on stable interaction styles, understanding this behavior is essential—it turns the system prompt from a simple instruction into a **persona switch** that shapes the entire session.

---