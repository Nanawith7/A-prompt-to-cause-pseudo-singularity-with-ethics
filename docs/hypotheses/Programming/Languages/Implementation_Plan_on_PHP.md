---
title: "Implementation Plan on PHP"
description: "A technical implementation plan for applying Deep Coding methodology to PHP projects, covering structural specification, generative conformance, validation gates, skeleton-tissue architecture, and recursive refinement using PHPStan, Deptrac, OpenAPI Generator, and Composer scripts."
author: "Nanawith7"
layout: default
categories: ["Software Engineering", "PHP", "AI-Assisted Development", "Specification-Driven Development"]
tags: ["deep_coding", "programming_languages", "generative_conformance", "structural_specification", "skeleton_tissue_architecture", "static_analysis", "static_analysis", "OpenAPI_Generator", "recursive_refinement"]
---

# Implementation Plan on PHP

## 1. Core Principles (Technical Translation)

| Deep Coding Principle | PHP Technical Equivalent |
|-----------------------|---------------------------|
| Intent–Structure–Implementation Separation | Interfaces + DI (structure) vs. concrete classes (implementation) |
| Generative Conformance | OpenAPI Generator + Nette PhpGenerator + validation gates |
| Recursive Refinement with Fixed Premises | Git tags + `FIXED_PREMISE.md` + phase branches |
| Skeleton–Tissue Architecture | `src/Skeleton/` (manual) + `src/Tissue/` (generated) + Deptrac |
| Validation Gates | PHPStan (level max) + Deptrac + PHPUnit + Symfony Validator |

## 2. Target Architecture

```
project-root/
├── spec/
│   ├── openapi.yaml          # API contract
│   └── schema/               # JSON Schema files
├── src/
│   ├── Skeleton/             # Manual, immutable
│   │   ├── Contracts/        # Interfaces
│   │   └── Base/             # Abstract classes (template methods)
│   ├── Tissue/               # AI-generated, regenerable
│   │   ├── Api/              # OpenAPI Generator output
│   │   ├── Repository/       # Concrete repositories
│   │   └── Service/          # Concrete services
│   └── Domain/               # Entities, value objects (manual)
├── tests/
│   ├── Unit/
│   ├── Architecture/         # Deptrac + PHPArkitect tests
│   └── Integration/
├── composer.json             # With automation scripts
├── phpstan.neon              # Level max configuration
├── deptrac.yaml              # Layer dependency rules
├── FIXED_PREMISE.md          # Phase checkpoint
└── .github/workflows/ci.yml
```

## 3. Phase-Based Workflow

Each phase follows: **Plan → Approve → Generate → Validate → Commit → Tag**

### Phase 0: Environment Setup
- Create directory structure
- Install dev dependencies: `phpstan/phpstan`, `deptrac/deptrac`, `phpunit/phpunit`, `symfony/validator`, `nette/php-generator`
- Configure `phpstan.neon` with level max and strict rules
- Configure `deptrac.yaml` (see Section 5)
- Add Composer scripts (see Section 6)

### Phase 1: Structural Specification
- Write OpenAPI YAML for all public APIs
- Define JSON Schema for data models
- Optionally add PHP attributes for business rules (e.g., Symfony Validator constraints)
- Validate: `openapi-generator validate -i spec/openapi.yaml`

### Phase 2: Skeleton Implementation (Manual)
- Create interfaces in `src/Skeleton/Contracts/`
- Implement abstract base classes with template methods
- Add cross-cutting concerns (logging, error handling) in skeleton
- Ensure no dynamic features (`__call`, `__get`, reflection) in skeleton
- Validate: PHPStan level max must pass

### Phase 3: Tissue Generation (AI + Tools)
- Run `openapi-generator generate -i spec/openapi.yaml -g php -o src/Tissue/Api`
- Generate DTOs from JSON Schema (custom script using Nette PhpGenerator)
- Generate repository/service stubs from interfaces
- Do not manually edit generated files

### Phase 4: Business Logic Implementation
- Implement concrete repositories and services in `src/Tissue/`
- Use dependency injection to consume skeleton interfaces
- Write unit tests (`phpunit`)
- Validate: PHPStan, Deptrac, PHPUnit (coverage ≥80%)

### Phase 5: Validation Gates (CI Integration)
All gates run automatically on `pre-commit` and in CI:

| Gate | Tool | Command |
|------|------|---------|
| Syntax | `php -l` | On staged PHP files |
| Static types | PHPStan | `phpstan analyse --level=max src/` |
| Architecture | Deptrac | `deptrac analyse` |
| Naming conventions | PHPArkitect | `phparkitect check` |
| Runtime validation | Symfony Validator | `phpunit --testsuite=validation` |
| Unit tests | PHPUnit | `phpunit --coverage-text` |

### Phase 6: Fixed Premise & Recursion
- After all gates pass, commit with message: `fix(premise): Phase N complete`
- Tag commit: `git tag phase-N-complete`
- Update `FIXED_PREMISE.md` with:
  - Current specification file hashes
  - Skeleton directory commit hash
  - Test suite results
- Next phase branches from this tag

## 4. Dependency Direction Enforcement (Deptrac)

```yaml
# deptrac.yaml
deptrac:
  paths: ["./src"]
  layers:
    - name: Skeleton
      collectors:
        - type: directory
          value: "./src/Skeleton/.*"
    - name: Tissue
      collectors:
        - type: directory
          value: "./src/Tissue/.*"
    - name: Domain
      collectors:
        - type: directory
          value: "./src/Domain/.*"
  ruleset:
    Tissue:
      - Skeleton
      - Domain
    Domain: ~
    Skeleton: ~
```

**Enforced property**: Tissue may depend on Skeleton and Domain, but never the reverse.

## 5. Composer Automation Scripts

```json
{
    "scripts": {
        "dc:validate": [
            "@dc:validate:static",
            "@dc:validate:architecture"
        ],
        "dc:validate:static": "phpstan analyse --level=max src/",
        "dc:validate:architecture": "deptrac analyse",
        "dc:generate:api": "openapi-generator generate -i spec/openapi.yaml -g php -o src/Tissue/Api",
        "dc:generate:dto": "php bin/generate-dto.php",
        "dc:generate:all": [
            "@dc:generate:api",
            "@dc:generate:dto"
        ],
        "dc:phase:complete": [
            "@dc:generate:all",
            "@dc:validate",
            "phpunit"
        ]
    }
}
```

## 6. Git Hooks (pre-commit)

```bash
#!/bin/sh
# .git/hooks/pre-commit
for file in $(git diff --cached --name-only --diff-filter=ACM | grep '\.php$'); do
    php -l "$file" || exit 1
done
composer dc:validate || exit 1
```

## 7. CI Pipeline (GitHub Actions)

```yaml
name: CI
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: shivammathur/setup-php@v2
        with: { php-version: '8.2' }
      - run: composer install
      - run: composer dc:validate
      - run: vendor/bin/phpunit --coverage-text
```

## 8. Constraints and Workarounds

| Constraint | Workaround |
|------------|------------|
| Single inheritance | Use interfaces + delegation instead of multiple abstract classes |
| Dynamic features (`__call`, `__get`) | Forbid in coding standards; detect with PHPStan custom rule |
| No built-in spec→code transform layer | Implement a small adapter using Nette PhpGenerator (reusable across projects) |
| Legacy codebases | Apply Deep Coding only to new modules; incrementally extract specifications |

## 9. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Skeleton modification count | 0 per phase | Git diff on `src/Skeleton/` |
| Static analysis pass rate | 100% | PHPStan exit code |
| Architecture rule violations | 0 | Deptrac exit code |
| Test pass rate | 100% | PHPUnit exit code |
| Human intervention per phase | < 10% of phases | Manual edits in `src/Tissue/` |

## 10. Conclusion

This implementation plan provides a concrete, toolchain-integrated pathway for applying Deep Coding to PHP projects. By encoding structural specifications in OpenAPI/JSON Schema, enforcing architectural constraints via Deptrac, validating types with PHPStan, and automating the recursive refinement workflow with Git tags and Composer scripts, PHP becomes a viable substrate for specification-driven, AI‑collaborative software development. The plan assumes PHP 8.2+, strict typing, and disciplined avoidance of dynamic features. When these conditions are met, the first generated tissue code becomes the final artifact for each phase, and long‑term maintainability is built into the process.
