---
title: "Implementation Plan on Dart"
description: "A technical framework for specification-driven software development in Dart, covering structural separation, generative conformance, skeleton-tissue architecture, validation gates, fixed premise management, and recursive refinement."
author: "Nanawith7"
layout: default
categories: ["Software Engineering", "Dart", "AI-Assisted Development"]
tags: ["Deep Coding", "Dart", "Specification-Driven", "Generative Conformance", "Skeleton-Tissue Architecture", "Validation Gates", "Code Generation", "Recursive Refinement", "Fixed Premise"]
---

# Implementation Plan on Dart

## 1. Core Principles (Technical Translation)

| Principle | Dart Implementation |
|-----------|---------------------|
| Intent–Structure–Implementation Separation | TypeScript interfaces → Dart `abstract interface class`; data models → `freezed`; API contracts → OpenAPI |
| Generative Conformance | `build_runner` + `source_gen` + `freezed` + `json_serializable` |
| Skeleton–Tissue Architecture | `base` class for skeleton (manual) + concrete classes (generated) |
| Recursive Refinement with Fixed Premises | Git tags + `pubspec.lock` + Melos workspaces |
| Validation Gates | `dart analyze` + `custom_lint` + `test_coverage` + `build_verify` |

## 2. Structural Specification Layer

### 2.1 API Boundaries (External)
- **Format**: OpenAPI 3.0+ YAML
- **Generation**: `openapi_generator` or `openapi-generator` (Dart client)
- **Location**: `specification/openapi/`

### 2.2 Data Models
- **Format**: Dart classes with `@freezed` and `@JsonSerializable()`
- **Generation**: `build_runner` produces `.g.dart` files
- **Runtime validation**: `json_schema3` (Draft 7) for JSON Schema conformance

### 2.3 Internal Module Contracts
- **Format**: `abstract interface class` (pure interface) or `base class` (with partial implementation)
- **Enforcement**: `custom_lint` rules forbid invalid dependencies

### 2.4 Directory Structure
```
lib/
├── specification/          # OpenAPI, JSON Schema, custom annotations
├── skeleton/               # Base classes (manual, never regenerated)
│   └── game_loop.dart      # base class with template method
├── tissue_src/             # Source files with generation annotations
│   └── models/
│       └── player.dart     # @freezed, @JsonSerializable()
└── tissue/                 # Generated code (.g.dart) - do not edit manually
```

## 3. Skeleton–Tissue Architecture

### 3.1 Skeleton Layer (Manual, Immutable)
- Use `base` modifier to prevent external implementation
- Template method pattern with `final` algorithm methods
- Cross-cutting concerns (logging, error handling, transaction boundaries)

```dart
// skeleton/game_loop.dart
base class GameLoopSkeleton {
  final void run() {
    onInitialize();
    while (isRunning) {
      onUpdate(deltaTime);
      onRender();
    }
    onDispose();
  }
  
  void onInitialize() {}
  void onUpdate(double dt) {}
  void onRender() {}
  void onDispose() {}
}
```

### 3.2 Tissue Layer (Generated)
- Concrete classes extending skeleton base classes
- Business logic implementations
- Generated from specifications using `build_runner`

```dart
// tissue_src/game_logic.dart
import 'package:my_app/skeleton/game_loop.dart';

part 'game_logic.g.dart';

@GenerateTissue()  // custom annotation
class GameLogic extends GameLoopSkeleton {
  @override
  void onUpdate(double dt) {
    // implementation generated or written
  }
}
```

### 3.3 Dependency Direction Enforcement
- `custom_lint` rule: `tissue` → `skeleton` allowed; reverse forbidden
- CI step: `dart run custom_lint` fails on violations

## 4. Generative Conformance

### 4.1 Code Generation Toolchain
- `build_runner` orchestrates generation
- `source_gen` provides AST-based generation API
- `freezed` + `json_serializable` produce immutable data classes

### 4.2 Configuration (`build.yaml`)
```yaml
targets:
  $default:
    builders:
      source_gen|combining_builder:
        generate_for:
          - lib/tissue_src/**.dart
      freezed|freezed:
        generate_for:
          - lib/tissue_src/models/**.dart
```

### 4.3 Generation Command
```bash
dart run build_runner build --delete-conflicting-outputs
```

## 5. Validation Gates

| Gate | Tool | Command | Fail Condition |
|------|------|---------|----------------|
| Format | `dart format` | `dart format --check .` | Unformatted code |
| Static analysis | `dart analyze` | `dart analyze --fatal-infos` | Any warning or info |
| Custom lint | `custom_lint` | `dart run custom_lint` | Dependency violation |
| Generation sync | `build_verify` | `dart run build_verify` | Outdated `.g.dart` files |
| Unit tests | `dart test` | `dart test --coverage` | Test failure |
| Coverage | `test_coverage` | `dart pub global run test_coverage --min-coverage 80` | Below threshold |

### 5.1 Analysis Options (`analysis_options.yaml`)
```yaml
include: package:lints/recommended.yaml
analyzer:
  language:
    strict-casts: true
    strict-inference: true
    strict-raw-types: true
linter:
  rules:
    - avoid_unused_constructor_parameters
    - cancel_subscriptions
```

### 5.2 Runtime Type Checking
- Use `is`, `as`, `runtimeType` for type tests
- For Flutter (no `dart:mirrors`): replace with `reflectable` (code‑generated reflection)

## 6. Fixed Premise Management

### 6.1 Components of a Fixed Premise
| Artifact | Purpose | Version Control |
|----------|---------|----------------|
| `pubspec.yaml` | Dependency declarations | Always |
| `pubspec.lock` | Exact versions (applications only) | Yes for apps, no for libraries |
| `analysis_options.yaml` | Static analysis rules | Always |
| `specification/` | OpenAPI, JSON Schema, interfaces | Always |
| `.g.dart` files | Generated code state | Always (with CI sync check) |
| Git tag | Phase boundary marker | `phase/1`, `phase/2`, … |

### 6.2 Phase Workflow
```bash
# Start from previous phase tag
git checkout phase/N-1
git checkout -b feature/phase-N

# 1. Update structural specification (OpenAPI, JSON Schema, interfaces)

# 2. Regenerate tissue
dart run build_runner build --delete-conflicting-outputs

# 3. Run validation gates
dart format --check .
dart analyze --fatal-infos
dart run custom_lint
dart run build_verify
dart test --coverage

# 4. Commit and tag
git add .
git commit -m "feat: Phase N implementation"
git tag phase/N
git push origin phase/N
```

### 6.3 Rollback
```bash
git checkout phase/N-1
dart pub get
dart run build_runner build
```

## 7. Monorepo Support with Melos

### 7.1 Workspace Structure
```
my_project/
├── pubspec.yaml              # workspace definition
├── packages/
│   ├── skeleton/             # base classes (manual)
│   ├── specification/        # OpenAPI, schemas
│   └── tissue/               # generated code (multiple packages)
└── apps/
    ├── mobile/               # Flutter app (with pubspec.lock)
    └── web/                  # web app
```

### 7.2 Melos Configuration (in root `pubspec.yaml`)
```yaml
name: my_project
workspace:
  - packages/*
  - apps/*
```

### 7.3 Essential Melos Commands
```bash
melos bootstrap          # install dependencies across all packages
melos run test           # run tests in all packages
melos version --yes      # bump versions based on conventional commits
```

## 8. Dart‑Specific Limitations and Workarounds

| Limitation | Workaround |
|------------|------------|
| No reflection in Flutter (`dart:mirrors`) | Use `reflectable` for code‑generated reflection; prefer compile‑time validation |
| Generated code placement (`.g.dart` + `part`) | Accept current pattern; future `external part` syntax will improve isolation |
| No built‑in Design by Contract | Enforce contracts via `base` classes, `custom_lint`, and runtime assertions |
| Flutter absolute path embedding | Not fully reproducible; accept functional reproducibility (same behavior, not bit‑identical) |
| Library vs application `pubspec.lock` | Only commit lock file for final applications, not for reusable tissue packages |

## 9. Implementation Checklist

- [ ] Enable `strict-*` options in `analysis_options.yaml`
- [ ] Create directory structure: `skeleton/`, `tissue_src/`, `specification/`
- [ ] Add `build_runner`, `freezed`, `json_serializable` to `pubspec.yaml`
- [ ] Write skeleton `base` classes with `final` template methods
- [ ] Annotate tissue source files with `@freezed` and `@JsonSerializable()`
- [ ] Configure `custom_lint` with dependency direction rule
- [ ] Set up CI pipeline: format → analyze → custom_lint → build_verify → test → coverage
- [ ] Define first fixed premise: commit + tag `phase/1`
- [ ] Iterate phases with recursive refinement

## 10. Conclusion

This implementation plan provides a complete, toolchain‑integrated pathway for applying specification‑driven development (Deep Coding) to Dart projects. Every principle translates to concrete Dart constructs:

- Structural specifications → OpenAPI, JSON Schema, `abstract interface class`
- Generative conformance → `build_runner` + `source_gen` + `freezed`
- Skeleton–tissue architecture → `base` classes + generated `.g.dart` files
- Validation gates → `dart analyze`, `custom_lint`, `test_coverage`, `build_verify`
- Fixed premises → `pubspec.lock` + Git tags
- Recursive refinement → Melos + Git worktree

The plan is executable in production Dart and Flutter projects. No philosophical axioms are required; all mechanisms are native to the Dart ecosystem.