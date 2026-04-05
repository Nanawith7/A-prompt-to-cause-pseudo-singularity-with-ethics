---
title: "Implementation Plan on Go"
description: "A technical implementation plan for applying specification-driven development methodology (Deep Coding) to Go projects, covering structural separation, generative conformance, skeleton-tissue architecture, validation gates, and recursive refinement with fixed premises."
author: "Nanawith7"
layout: default
categories: ["Software Engineering", "Go", "AI-Assisted Development"]
tags: ["Deep Coding", "Go", "Specification-Driven", "Generative Conformance", "Skeleton-Tissue Architecture", "Validation Gates", "Recursive Refinement", "Fixed Premise", "Code Generation"]
---

# Implementation Plan on Go

## 1. Overview

This plan defines how to implement a specification-driven development methodology (referred to as Deep Coding) in Go. The methodology is built on four technical pillars:

- **Structural separation** – Intent, specification, and implementation are distinct layers.
- **Generative conformance** – Implementation is generated from a structural specification and automatically verified.
- **Skeleton–tissue architecture** – Invariant control flow (skeleton) is manually maintained; variable logic (tissue) is generated.
- **Recursive refinement with fixed premises** – Development proceeds in phases; each phase commits a fixed premise (versioned specification + dependencies) and refines iteratively.

All philosophical framing is replaced with executable Go constructs and toolchain integrations.

---

## 2. Core Principles to Go Mapping

| Principle | Go Implementation | Tooling / Pattern |
|-----------|------------------|--------------------|
| Structural separation | Interfaces (consumer‑defined) + packages | Standard library |
| Generative conformance | Code generation from OpenAPI / JSON Schema | `go generate`, oapi-codegen |
| Skeleton–tissue architecture | Control‑flow functions + interface callbacks | Custom pattern (no inheritance) |
| Validation gates | Static analysis + custom analyzers + tests | `go vet`, `go/analysis`, `golangci-lint` |
| Fixed premise | Version‑locked dependencies + vendoring | `go.mod`, `vendor/`, Git tags |
| Recursive refinement | Workspaces + API compatibility checks | `go.work`, `apidiff`, Git worktree |

---

## 3. Structural Specification Layer

The specification is expressed in machine‑readable formats and stored under `specification/`.

| Scope | Format | Tool |
|-------|--------|------|
| API boundaries (REST) | OpenAPI 3.0+ YAML | oapi-codegen |
| Data models | JSON Schema | `jsonschema` + codegen |
| Internal module contracts | Go interfaces (manual) | `go/analysis` for enforcement |

**Selection rule**: Prefer OpenAPI for external APIs, JSON Schema for shared data, and Go interfaces for internal boundaries.

Example specification (OpenAPI fragment):
```yaml
openapi: 3.0.3
paths:
  /players/{id}:
    get:
      operationId: getPlayer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Player'
```

---

## 4. Generative Conformance

Code generation transforms the structural specification into conforming implementation.

**Workflow**:
1. Define/update specification files.
2. Run `go generate ./...` (directives in source).
3. Generated code is placed in `tissue/generated/` with `// Code generated ... DO NOT EDIT.` header.
4. CI checks that generated code is up‑to‑date (`git diff --exit-code`).

**Key tools**:
- `oapi-codegen` – generates Go server/client code with built‑in validation from OpenAPI schemas.
- `go generate` – native mechanism; can invoke any command.
- `stringer` / `enumer` – for enum string conversion.

**Validation gates after generation**:
- `go build` – catches type errors.
- `go vet` with custom analyzers – catches layer violations.
- `go test` – runs runtime validation.

---

## 5. Skeleton–Tissue Architecture (Go‑Specific)

Go has no inheritance, so the classical template method pattern is replaced with **control‑flow functions + interface callbacks**.

### 5.1 Skeleton Layer (Manual, Immutable)

The skeleton owns the execution flow. It is written once by humans and never modified by AI.

**Pattern: Control‑flow function**
```go
// skeleton/runner.go
package skeleton

type Steps interface {
    Initialize() error
    Update(delta float64) error
    Render() error
    Cleanup() error
}

// RunLoop owns the execution order.
func RunLoop(steps Steps) error {
    if err := steps.Initialize(); err != nil {
        return err
    }
    defer steps.Cleanup()
    for running {
        if err := steps.Update(delta); err != nil {
            return err
        }
        if err := steps.Render(); err != nil {
            return err
        }
    }
    return nil
}
```

**Enforcing immutability**:
- Place skeleton code in `skeleton/` package.
- Use custom `go/analysis` analyzer to forbid imports from `skeleton/` to `tissue/` (reverse dependency).
- Code review and CI reject changes to `skeleton/` without explicit approval.

### 5.2 Tissue Layer (Generated or AI‑produced)

The tissue implements the `Steps` interface. It is fully generated from the structural specification.

```go
// tissue/game_impl.go (generated)
package tissue

type GameImpl struct {
    // fields from specification
}

func (g *GameImpl) Initialize() error { /* generated */ }
func (g *GameImpl) Update(delta float64) error { /* generated */ }
func (g *GameImpl) Render() error { /* generated */ }
func (g *GameImpl) Cleanup() error { /* generated */ }
```

**Compile‑time interface verification** (idiom):
```go
var _ skeleton.Steps = (*tissue.GameImpl)(nil)
```

### 5.3 Dependency Direction Enforcement

- Skeleton depends on nothing.
- Tissue depends on skeleton (imports `skeleton` package).
- Use `go-arch-lint` or a custom `go/analysis` analyzer to enforce:
  - `tissue` → `skeleton` allowed.
  - `skeleton` → `tissue` forbidden.
  - No circular dependencies (already enforced by Go compiler).

---

## 6. Validation Gates

Four layers of automated validation ensure conformance.

| Layer | Tool | Command | Fail Condition |
|-------|------|---------|----------------|
| Compile‑time | `go build` | `go build ./...` | Type error, cycle |
| Static analysis | `go vet` + custom analyzers | `go vet -vettool=... ./...` | Layer violation, naming convention |
| Lint | `golangci-lint` | `golangci-lint run` | Code quality issues |
| Runtime | `go test` | `go test -race -cover ./...` | Failed tests, race conditions |

**Custom analyzer example** (layer dependency check):
```go
// analyzers/layercheck.go
var Analyzer = &analysis.Analyzer{
    Name: "layercheck",
    Run: func(pass *analysis.Pass) (interface{}, error) {
        // Forbid skeleton imports from tissue
        for _, f := range pass.Files {
            for _, imp := range f.Imports {
                if isSkeleton(pass.Pkg.Path()) && isTissue(imp.Path.Value) {
                    pass.Reportf(imp.Pos(), "skeleton cannot import tissue")
                }
            }
        }
        return nil, nil
    },
}
```

**CI integration**: All gates must pass before merging. Generated code freshness is checked via `git diff --exit-code` after `go generate`.

---

## 7. Fixed Premise Management

A fixed premise is the immutable state after a completed phase: specification files, dependencies, and tool versions.

**Components**:
- `go.mod` + `go.sum` – exact dependency versions (semantic versioning).
- `vendor/` – complete copy of all dependencies (committed to repo for full reproducibility).
- `go.work` (optional) – local workspace for multi‑module development.
- Git tag – marks phase boundary (e.g., `phase/1`).

**Phase completion checklist**:
```bash
go test -race -cover ./...
go mod tidy
go mod vendor
git add go.mod go.sum vendor/ specification/
git commit -m "Phase N: <summary>"
git tag phase/N
```

**Rollback**: `git checkout phase/N-1 && go mod vendor` restores previous state.

**Go version pinning** (Go 1.21+):
```go
// go.mod
go 1.21
toolchain go1.21.8
```
Set `GOTOOLCHAIN=local` in CI to prevent automatic upgrades.

---

## 8. Recursive Refinement Workflow

Each phase refines the specification and regenerates the tissue.

**Phase steps**:
1. **Plan** – Define changes to structural specification (OpenAPI, JSON Schema, interfaces).
2. **Generate** – Run `go generate ./...` to produce/update tissue code.
3. **Validate** – Execute all validation gates (build, vet, lint, test).
4. **Commit** – If all pass, commit new specification + generated code as fixed premise (Git tag).
5. **Repeat** – Next phase.

**Parallel phase development** (Git worktree):
```bash
git worktree add -b phase/2 ../project-phase2 main
git worktree add -b phase/3 ../project-phase3 main
```

**API compatibility check** between phases:
```bash
apidiff phase/1/package phase/2/package
```

**Impact analysis** (which packages are affected by a change):
```bash
go list -deps ./... | grep changed-package
```

---

## 9. Toolchain Summary

| Purpose | Tool | Version requirement |
|---------|------|---------------------|
| Build & test | Go compiler | 1.21+ (toolchain directive) |
| Code generation | `go generate` + oapi-codegen | oapi-codegen v2 |
| Static analysis | `go vet` + custom analyzers | Go 1.18+ (go/analysis) |
| Linter | golangci-lint | latest |
| Dependency vendoring | `go mod vendor` | built‑in |
| Workspace | `go.work` | Go 1.18+ |
| API compatibility | apidiff | `golang.org/x/tools/cmd/apidiff` |
| Architecture rules | go-arch-lint or custom analyzer | optional |
| Git worktree | Git | 2.5+ |

---

## 10. Limitations and Mitigations

| Limitation | Mitigation |
|------------|------------|
| No compile‑time design‑by‑contract | Use interface + runtime assertions + extensive unit tests |
| No `final` methods / guaranteed ownership | Control‑flow functions + code review + custom analyzer |
| No inheritance for template method | Use strategy pattern + callback interfaces |
| Generic methods on interfaces not allowed (pre‑1.26) | Use generic functions or type‑specific interfaces |
| `go.work` not recommended for CI | Use separate `go.mod` per module in CI; `go.work` only for local development |
| Reflection‑heavy libraries may bypass skeleton | Restrict Deep Coding to contract layer; keep adapters for external libs |

---

## 11. Implementation Checklist

- [ ] Enable `go.mod` with `toolchain` directive.
- [ ] Create directory structure: `specification/`, `skeleton/`, `tissue/generated/`.
- [ ] Write OpenAPI/JSON Schema specifications.
- [ ] Configure oapi-codegen with `go:generate` directives.
- [ ] Implement skeleton control‑flow functions (manual, in `skeleton/`).
- [ ] Generate tissue code and verify compilation.
- [ ] Write custom `go/analysis` analyzer for layer rules.
- [ ] Set up `golangci-lint` with custom rules.
- [ ] Add CI pipeline: `go generate`, `git diff`, `go vet`, `golangci-lint`, `go test`.
- [ ] Define first fixed premise: commit + tag `phase/1`.
- [ ] Iterate phases recursively.

---

## 12. Conclusion

Go provides all necessary mechanisms to implement a specification‑driven methodology (Deep Coding) without relying on inheritance or philosophical axioms. The combination of:

- **Interfaces** for structural separation,
- **`go generate` + oapi-codegen** for generative conformance,
- **Control‑flow functions** as a substitute for template methods,
- **`go/analysis`** for custom validation gates,
- **`go.mod` + vendor + Git tags** for fixed premises,
- **`go.work` + Git worktree** for recursive refinement,

forms a complete, production‑ready implementation plan. The resulting process eliminates implementation‑level bugs caused by interface mismatches, enables safe refactoring through specification‑only changes, and keeps context cost independent of codebase size.