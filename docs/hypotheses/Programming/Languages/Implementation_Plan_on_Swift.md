---
title: "Implementation Plan on Swift"
description: "A technical framework for applying specification‑driven, AI‑assisted development to Swift projects. Defines structural separation, generative conformance, recursive refinement, skeleton‑tissue architecture, and validation gates using Swift language features and toolchain."
author: "Nanawith7"
layout: default
categories: ["Software Engineering", "Swift", "AI‑Assisted Development"]
tags: ["deep_coding", "Swift", "generative_conformance", "structural_specification", "validation_gates", "Skeleton‑Tissue_Architecture", "recursive_refinement", "SwiftPM"]
---

# Implementation Plan on Swift

## 1. Core Principles to Swift Mapping

| Principle | Swift Implementation | Supporting Tools |
|-----------|----------------------|------------------|
| Intent‑Structure‑Implementation Separation | Protocol (specification) + Protocol extension (skeleton) + Concrete type (tissue) | Swift compiler |
| Generative Conformance | Code generation from OpenAPI / JSON Schema / protocols | Swift OpenAPI Generator, Sourcery, Swift macros |
| Recursive Refinement with Fixed Premises | Module stability + library evolution + Git tags | SwiftPM, `swift-api-digester` |
| Skeleton‑Tissue Architecture | Abstract protocols + `final` template methods + conforming structs/classes | Access control, `actor` |
| Validation Gates | Static analysis + linting + dependency graph + runtime checks | Swift compiler flags, SwiftLint, spmgraph, XCTest |

## 2. Architecture Layers

```
Layer 0: Intent (Human)
   ↓
Layer 1: Structural Specification
   - OpenAPI / JSON Schema / Swift protocols / Codable
   - Stored in `Specification/`
   ↓
Layer 2: Code Generation
   - Swift OpenAPI Generator, Sourcery, Swift macros
   - Output to `Generated/` (tissue)
   ↓
Layer 3: Validation Gates
   - Compiler (`swift build -c release`)
   - SwiftLint (`swiftlint lint --strict`)
   - spmgraph (`spmgraph lint --strict`)
   - Runtime tests (`swift test`)
   ↓
Layer 4: Tissue (Generated) + Skeleton (Manual)
   - Tissue: `Sources/Tissue/` – business logic, concrete implementations
   - Skeleton: `Sources/Skeleton/` – protocols, abstract classes, cross‑cutting concerns
```

## 3. Structural Specification Formats

| Scope | Format | Tooling |
|-------|--------|---------|
| API boundaries (REST) | OpenAPI 3.0+ YAML | Swift OpenAPI Generator (Apple) |
| Data models | JSON Schema | `json‑schema‑to‑swift` or custom SwiftSyntax generator |
| Internal module contracts | Swift protocols | Compiler + Sourcery |
| Runtime‑validated boundaries | Codable + Sendable | Swift standard library |
| Full‑stack Swift | gRPC / Protobuf | Swift Protobuf |

**Selection rule**: OpenAPI for external APIs, JSON Schema for shared data, protocols for internal modules.

## 4. Skeleton‑Tissue Pattern in Swift

### 4.1 Skeleton (Manual, Immutable)

Protocols with template methods implemented in protocol extensions. The template method is marked `final` to prevent tissue overrides.

```swift
// Skeleton/GameLoopSkeleton.swift
public protocol GameLoopSkeleton {
    func setup()
    func update(deltaTime: Double)
    func render()
    func cleanup()
}

public extension GameLoopSkeleton {
    final func run() {
        setup()
        while isRunning {
            update(deltaTime: currentDelta)
            render()
        }
        cleanup()
    }
}
```

### 4.2 Tissue (Generated or AI‑produced)

Concrete types conforming to skeleton protocols. Located in `Sources/Tissue/`.

```swift
// Tissue/GameLogic.swift (generated)
import Skeleton

public struct GameLogic: GameLoopSkeleton {
    public func setup() { /* generated */ }
    public func update(deltaTime: Double) { /* generated */ }
    public func render() { /* generated */ }
    public func cleanup() { /* generated */ }
}
```

### 4.3 Concurrency‑Aware Skeleton (Actor)

For thread‑safe skeletons, use `actor` instead of protocol.

```swift
public actor ServiceSkeleton {
    public final func execute(request: Request) async throws -> Response {
        let validated = try await validate(request)
        let result = try await process(validated)
        return result
    }
    public func validate(_ request: Request) async throws -> ValidatedRequest
    public func process(_ validated: ValidatedRequest) async throws -> Response
}
```

## 5. Validation Gates (Four Layers)

| Layer | Tool | Command | Enforcement |
|-------|------|---------|-------------|
| Compile‑time | Swift compiler | `swift build -c release -strict-concurrency=complete` | Type safety, actor isolation, Sendable |
| Lint‑time | SwiftLint (custom rules) | `swiftlint lint --strict` | Import restrictions, naming, style |
| Dependency | spmgraph | `spmgraph lint --strict` | Module dependency direction, circular imports |
| Runtime | XCTest | `swift test` | Protocol conformance, contract validation |

**CI integration (GitHub Actions)**:

```yaml
- name: Compile
  run: swift build -c release
- name: Lint
  run: swiftlint lint --strict
- name: Dependency audit
  run: spmgraph lint --strict
- name: Test
  run: swift test
```

## 6. Recursive Refinement with Fixed Premises

### 6.1 Fixed Premise Definition

A fixed premise is a versioned snapshot of the structural specification (protocols, OpenAPI files, JSON Schema) plus the skeleton code. It is treated as immutable within a phase.

### 6.2 Workflow per Phase

```
Phase N complete
    │
    ├── Enable module stability
    │   swift build -c release -Xswiftc -enable-library-evolution
    │
    ├── Record API baseline
    │   xcrun swift-api-digester -module SkeletonModule -o baseline.json
    │
    ├── Tag fixed premise
    │   git tag phase-N-complete
    │
    ▼
Modify structural specification
    │
    ├── Detect breaking changes
    │   swift package diagnose-api-breaking-changes phase-N-complete
    │   → if breaking, require major version bump
    │
    ├── Regenerate tissue
    │   sourcery --config .sourcery.yml
    │
    ├── Incremental build
    │   swift build -c release
    │
    ▼
Phase N+1 complete
    │
    └── git tag phase-N+1-complete
```

### 6.3 Parallel Phases with Git Worktree

```bash
git worktree add ../project-phase2 phase2-branch
git worktree add ../project-phase3 phase3-branch
```

## 7. Code Generation Tools

| Tool | Approach | Use Case |
|------|----------|----------|
| **Swift OpenAPI Generator** | OpenAPI → Swift client/server | API boundaries (external) |
| **Sourcery** | Source code + Stencil templates → Swift | Internal protocol conformance, mocks |
| **Swift macros (Swift 5.9+)** | AST‑level expansion | Boilerplate reduction (`@AutoCodable`) |
| **SwiftSyntax** | Programmatic AST generation | Custom generators for JSON Schema |

**Recommendation**: Start with Swift OpenAPI Generator for API layers and Sourcery for internal modules. Use macros only for high‑value repetitive patterns.

## 8. Dependency Injection for Skeleton‑Tissue Coupling

Two compile‑time safe approaches:

| Approach | Mechanism | Pros | Cons |
|----------|-----------|------|------|
| **Needle** | Code generation from protocol + Component definitions | True compile‑time safety, proven at Uber scale | Requires extra build step, existential `any` issues |
| **swift-dependencies** | `@Dependency` property wrapper + `DependencyValues` | Swift‑native, no generation | Runtime resolution, ties to TCA |

**Implementation guideline**: Use Needle for phase 0‑1 to enforce strict separation. Plan for optional migration to swift-dependencies if language evolution creates friction.

## 9. Swift‑Specific Adaptations

| Swift Feature | Deep Coding Application |
|---------------|-------------------------|
| **Protocol + protocol extension** | Template method pattern without inheritance |
| **Actor** | Thread‑safe skeleton for concurrent execution |
| **Value types (struct, enum)** | Tissue business logic with localised side effects |
| **Access control (`public`, `internal`, `private import`)** | Enforce skeleton‑tissue dependency direction |
| **Module stability + library evolution** | Fixed premise versioning and binary compatibility |
| **Swift macros** | Generate tissue conformance from protocol specifications |
| **Sendable** | Enforce safe data transfer across actor boundaries |

## 10. Implementation Phases and Timeline

| Phase | Scope | Deliverable | Duration |
|-------|-------|-------------|----------|
| 0 | Infrastructure | SwiftPM multi‑module layout, SwiftLint + spmgraph CI | 1 month |
| 1 | Skeleton design | Protocols + protocol extensions + actor skeletons | 1.5 months |
| 2 | Structural specification | OpenAPI / JSON Schema / Codable models | 1 month |
| 3 | Generation pipeline | Sourcery templates + Swift OpenAPI Generator | 1.5 months |
| 4 | Validation gates | Custom SwiftLint rules + spmgraph config + API breaking detection | 1 month |
| 5 | Pilot project | Apply to one module, measure regeneration time and bug rates | 1‑2 months |

**Total**: 6‑9 months for full adoption.

## 11. Constraints and Mitigations

| Constraint | Mitigation |
|------------|-------------|
| Code generation tools have learning curves | Start with Sourcery (template‑based) before moving to macros |
| Needle’s compatibility with Swift 6+ | Maintain swift-dependencies as fallback; test with existential `any` |
| spmgraph is relatively new | Complement with `depermaid` for visualisation; use compiler‑level checks as primary |
| Module stability requires careful API design | Limit skeleton surface area; plan major version upgrades explicitly |
| Runtime protocol conformance checks are costly | Prioritise compile‑time validation; use `FastCast` caching if dynamic checks required |

## 12. Summary

Swift provides all necessary language features and tooling to implement a specification‑driven, AI‑assisted development workflow:

- **Structural separation** via protocols and protocol extensions
- **Generative conformance** via Swift OpenAPI Generator, Sourcery, and macros
- **Recursive refinement** via module stability, API digester, and Git tags
- **Skeleton‑tissue architecture** via protocols + actors (skeleton) and conforming value types (tissue)
- **Validation gates** via compiler flags, SwiftLint, spmgraph, and XCTest

The resulting methodology enables human developers to define invariant architectural skeletons while generated code (tissue) handles business logic. Each phase produces a fixed premise that guarantees backward compatibility, and changes propagate through automatic regeneration and validation. This approach is ready for production use in server‑side Swift, iOS applications, and SwiftUI projects.