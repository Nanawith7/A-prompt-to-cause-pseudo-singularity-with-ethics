---
title: "Partial Implementation Plan on Lua"
description: "A technical framework for applying specification-driven, AI-assisted development methodology to Lua projects under language constraints. Defines structural specifications via JSON Schema and Teal records, skeleton-tissue separation, four-layer validation gates, recursive refinement with fixed premises, and evaluation metrics. Focuses on implementable subsets without full static typing."
author: "Nanawith7"
layout: default
categories: ["Software Engineering", "Lua", "Specification-Driven Development", "AI-Assisted Development"]
tags: ["programming_languages", "deep_coding", "Partial_Implementation", "structural_specification", "Teal", "skeleton_tissue_architecture", "validation_gates", "fixed_premise"]
---

# Partial Implementation Plan on Lua

## 1. Scope

This document defines a partial implementation plan for applying specification-driven, AI‑assisted development to Lua projects. Full implementation of the methodology requires static typing and language‑enforced dependency control, which Lua does not provide. The following subset is implementable:

- Structural specification via JSON Schema and Teal records
- Skeleton‑tissue separation through directory conventions and CI checks
- Four‑layer validation gates (type check, lint, unit test, coverage)
- Recursive refinement with fixed premises (Git tags + Markdown)
- Generative conformance using Teal’s `tl gen` pipeline

## 2. Core Principles (Technical Translation)

| Principle | Lua Technical Implementation |
|-----------|------------------------------|
| Structural specification | JSON Schema for data + Teal record types for interfaces |
| Generative conformance | Teal type definitions → `tl gen` → standard Lua code |
| Skeleton‑tissue separation | Directory split (`skeleton/` vs `tissue/`) + CI dependency checks |
| Recursive refinement | Git tags + `FIXED_PREMISE.md` + phase‑based commits |
| Validation gates | `tl check`, `luacheck`, `busted`, `luacov` in CI pipeline |

## 3. Structural Specification Layer

Two complementary representations:

- **JSON Schema** – defines data structures, validation rules, and serialization contracts.
- **Teal record types** – defines function signatures, interface contracts, and type aliases.

These two sources are maintained manually in the `spec/` directory. Consistency between them is verified during validation.

Example `spec/config.tl`:
```teal
local record Config
    score: integer
    lives: integer
    invincible_frames: integer
end

local record GameLoop
    update: function(Config, number) -> Config
    render: function(Config)
end
```

## 4. Skeleton–Tissue Architecture

**Directory structure:**

```
project/
├── skeleton/          # Hand‑written, immutable (human only)
│   ├── loader.lua
│   └── validator.lua
├── spec/              # Structural specifications
│   ├── config.schema.json
│   └── config.tl
├── tissue/            # AI‑generated, regenerable
│   ├── parser.tl      # Generated from spec
│   └── parser.lua     # Output of `tl gen`
├── tests/             # Busted test suite
├── FIXED_PREMISE.md
└── .github/workflows/ci.yml
```

**Dependency rule:** Code in `skeleton/` must not `require` any module from `tissue/`. CI enforces this with `grep`.

**Template method pattern (skeleton controls execution flow):**

```lua
-- skeleton/loader.lua
local Loader = {}
function Loader.run(impl, input)
    impl:init()
    local result = impl:process(input)
    impl:cleanup()
    return result
end
return Loader
```

Tissue code provides the `init`, `process`, `cleanup` methods and is generated from the structural specification.

## 5. Validation Gates (4 Layers)

| Layer | Tool | Command | Pass Condition |
|-------|------|---------|----------------|
| L1: Type check | Teal | `tl check tissue/*.tl` | 0 errors |
| L2: Lint | luacheck | `luacheck .` | 0 warnings |
| L3: Unit tests | Busted | `busted --coverage tests/` | 100% pass |
| L4: Coverage | LuaCov | integrated with Busted | ≥80% |
| L5: Dependency direction | grep | `grep -r "require.*tissue" skeleton/` | 0 matches |

CI workflow (GitHub Actions) runs all gates on every push and pull request.

## 6. Recursive Refinement with Fixed Premises

Development proceeds in phases. Each phase ends with a **fixed premise**:

- A Git tag named `phase-N-complete`
- A `FIXED_PREMISE.md` file containing:
  - Phase number and date
  - Current specification file hashes
  - Skeleton commit hash
  - Validation gate results
  - Allowed changes for the next phase

Subsequent phases treat the fixed premise as immutable. Changes to the specification must be explicitly planned and approved before the next phase.

**Phase workflow:**

1. Plan specification changes (JSON Schema and/or Teal records)
2. Human approval of the delta
3. AI generates tissue code (`.tl` files) from updated spec
4. Run validation gates
5. If all gates pass, commit new spec, generated code, and update `FIXED_PREMISE.md` with a new tag
6. Repeat

## 7. Evaluation Metrics

| Metric | Target | Collection Method |
|--------|--------|-------------------|
| Skeleton modifications | 0 per phase | `git diff --name-only skeleton/` |
| Type check pass rate | 100% | CI exit code |
| Test pass rate | 100% | CI exit code |
| Code coverage | ≥80% | luacov report |
| Regeneration iterations | ≤3 per phase | CI log analysis |
| Specification change lead time | <15 minutes | CI execution time |
| Human intervention ratio | <10% of phases | Project log |

## 8. Implementation Layer Comparison

| Layer | Standard Lua | With Teal | With Luau |
|-------|--------------|-----------|-----------|
| Static type checking | Not available | `tl check` | `luau-analyze` |
| Runtime overhead | None | None (types removed) | Present (type info retained) |
| Generation pipeline | Manual | `tl gen` from Teal | Limited conversion tools |
| Runs on standard Lua VM | Yes | Yes (after generation) | No (requires Luau VM) |
| Learning curve | Low | Medium | Medium (Roblox‑specific) |

**Recommended baseline for partial implementation:** Teal. It provides static checking during development and produces standard Lua code with zero runtime overhead.

## 9. Pilot Project Specification

**Target:** CLI tool that generates Lua tables from JSON configuration files.

**Phases (6 phases, estimated 4–5 person‑days):**

| Phase | Focus | Specification Change | Generated Output |
|-------|-------|----------------------|------------------|
| 0 | Skeleton implementation | None (manual) | `skeleton/loader.lua`, `validator.lua` |
| 1 | JSON Schema definition | `spec/config.schema.json` | None |
| 2 | Teal record definition | `spec/config.tl` | None |
| 3 | Parser generation | Spec finalized | AI generates `tissue/parser.tl` |
| 4 | Validation logic | Add validation rules | AI extends `validator` |
| 5 | CI integration | Workflow definition | `.github/workflows/ci.yml` |

Each phase ends with a fixed premise commit and tag.

## 10. Constraints and Workarounds

| Constraint | Workaround |
|------------|-------------|
| No native static types | Use Teal records and `tl check` during development |
| No language‑enforced dependency direction | CI grep check + directory conventions |
| Limited JSON Schema → Lua code generators | Use `presilo` (requires Go) or manual template |
| No unified schema definition (like pydantic) | Maintain JSON Schema + Teal records; future tooling can sync them |
| Metaprogramming reduces analyzability | Restrict metatable usage to skeleton layer only |

## 11. Toolchain Requirements

- **Teal** – `tl` compiler (type checking and code generation)
- **luacheck** – static analyzer and linter
- **Busted** – unit test framework
- **LuaCov** – code coverage (integrated with Busted)
- **Git** – version control and fixed premise management
- **GitHub Actions** – CI pipeline (or any CI with Lua support)

Optional:
- **Xmake** – Lua‑based build automation (replaces Makefile)
- **presilo** – JSON Schema → Lua code generation

## 12. Summary

A partial implementation of specification‑driven, AI‑assisted development is achievable in Lua through:

- Teal for static type checking and code generation
- Directory‑based skeleton‑tissue separation enforced by CI
- Four‑layer validation gates (type, lint, test, coverage)
- Phase‑based recursive refinement with fixed premises

This plan defines executable procedures, evaluation metrics, and a pilot scope. Full static typing remains unavailable in standard Lua, but Teal provides a practical approximation without runtime overhead.