---
title: "Partial Implementation Plan on Matlab"
description: "A technical specification for applying specification-driven, AI-assisted software development methodology to MATLAB projects. Defines structural specification using JSON Schema, generative conformance via function handles and unit tests, skeleton-tissue architecture with template method or function injection, recursive refinement with Git tags and fixed premise files, and validation gates using checkcode, miss_hit, and matlab.unittest."
author: "Nanawith7"
layout: default
categories: ["Software Engineering", "MATLAB", "AI-Assisted Development", "Specification-Driven Development"]
tags: ["deep_coding", "MATLAB", "structural_specification", "generative_conformance", "skeleton_tissue_architecture", "Function_Handle", "validation_gates", "recursive_refinement"]
---

# Partial Implementation Plan on Matlab

## 1. Overview

This plan translates the four principles of Deep Coding – structural specification, generative conformance, recursive refinement, and skeleton‑tissue architecture – into MATLAB‑compatible constructs. MATLAB’s dynamic typing and object‑oriented overhead prevent full implementation. The plan therefore defines a **partial, lightweight** version using function handles, MVC patterns, and existing static analysis tools.

## 2. Core Principles (Technical Restatement)

| Deep Coding Principle | MATLAB Realization |
|-----------------------|---------------------|
| Structural specification | JSON Schema + `ansatz27` or `functionSignatures.json` |
| Generative conformance | Function handle injection + `matlab.unittest` verification |
| Skeleton‑tissue separation | Template method (abstract class) or function handle injection |
| Recursive refinement | Git tags + `FIXED_PREMISE.md` + dependency analysis |

## 3. Structural Specification

Define machine‑readable contracts using:

- **JSON Schema** – data structures, invariants, and API shapes.  
  Use `ansatz27` (third‑party) to validate MATLAB structs against the schema.
- **`functionSignatures.json`** – function argument types and return values.  
  Validate with `validateFunctionSignaturesJSON`.
- **Property validation** – `mustBeNumeric`, `mustBeFinite`, etc., inside `classdef`.

Example JSON Schema (`specification/game_state.schema.json`):
```json
{
  "type": "object",
  "properties": {
    "score": { "type": "integer", "minimum": 0 },
    "lives": { "type": "integer", "minimum": 0, "maximum": 5 }
  },
  "required": ["score", "lives"]
}
```

## 4. Generative Conformance

Implementation code is generated from the specification. MATLAB lacks native code generation from JSON Schema, so the AI produces MATLAB code that is **verified against** the specification.

**Pipeline**:
1. Update JSON Schema (structural specification).
2. AI generates function handle or class method that consumes/produces data matching the schema.
3. Validation gate runs:
   - `checkcode` – syntax errors.
   - `miss_hit` (`mh_lint`, `mh_style`) – static quality.
   - `matlab.unittest` – runtime conformance test using schema validator.

**Example conformance test**:
```matlab
function testConformsToSchema(testCase)
    import matlab.unittest.constraints.IsEqualTo;
    data = tissueFunction();  % generated tissue
    schema = jsondecode(fileread('specification/game_state.schema.json'));
    % ansatz27 validation
    isValid = ansatz27.validate(data, schema);
    testCase.verifyTrue(isValid, 'Generated data does not conform to schema');
end
```

## 5. Skeleton‑Tissue Patterns

Two patterns support separation of invariant skeleton (human‑maintained) from generated tissue.

### 5.1 Function Handle Injection (Low Overhead)

Skeleton owns execution flow, tissue is a pure function.

**Skeleton** (manual, immutable):
```matlab
classdef ProcessorSkeleton < handle
    properties (Access = private)
        tissueFn
    end
    methods
        function obj = ProcessorSkeleton(tissueFn)
            obj.tissueFn = tissueFn;
        end
        function result = process(obj, input)
            validated = obj.validate(input);
            result = obj.tissueFn(validated);
            result = obj.postprocess(result);
        end
    end
    methods (Access = private)
        function out = validate(~, in), out = in; end
        function out = postprocess(~, in), out = in; end
    end
end
```

**Tissue** (AI‑generated from specification):
```matlab
% Generated from JSON Schema
myTissue = @(x) struct('score', x.score + 10, 'lives', x.lives);
processor = ProcessorSkeleton(myTissue);
```

### 5.2 Template Method (Abstract Class)

Use when multiple tissue implementations share the same skeleton.

**Skeleton**:
```matlab
classdef (Abstract) GameLoopSkeleton < handle
    methods (Abstract)
        update(obj, dt)
        render(obj)
    end
    methods
        function run(obj)
            while true
                dt = toc;
                tic;
                obj.update(dt);
                obj.render();
                drawnow;
            end
        end
    end
end
```

**Tissue** (concrete subclass generated by AI):
```matlab
classdef MyGame < GameLoopSkeleton
    methods
        function update(obj, dt)
            % generated logic
        end
        function render(obj)
            % generated logic
        end
    end
end
```

## 6. Recursive Refinement and Fixed Premises

Development proceeds in phases. After each phase, commit a **fixed premise** – a snapshot of the current specification and skeleton.

**Fixed premise structure** (`FIXED_PREMISE.md`):
```markdown
# Fixed Premise – Phase N
- Git tag: phase-N-complete
- Specification hash: (commit hash of specification/ folder)
- Skeleton hash: (commit hash of skeleton/ folder)
- Validation gate results: checkcode 0 errors, test pass 100%
- Next phase allowed changes: [list of spec sections modifiable]
```

**Workflow**:
1. Start from tag `phase-N-complete`.
2. Modify JSON Schema only.
3. Run generation and validation gates.
4. If all pass, commit new specification and generated tissue, create tag `phase-N+1-complete`.
5. Repeat.

**Dependency analysis** – Use MATLAB Dependency Analyzer to detect accidental tissue→skeleton reverse dependencies. Export graph and enforce direction in CI.

## 7. Validation Gates

All generated code must pass the following automated checks before phase completion.

| Gate | Tool | Command | Pass Condition |
|------|------|---------|----------------|
| Syntax | `checkcode` | `checkcode('tissue/','-config=onlyErrors.txt')` | 0 errors |
| Style & complexity | `miss_hit` | `mh_style tissue/ && mh_metric --ci tissue/` | 0 violations, cyclomatic complexity < 10 |
| Unit tests | `matlab.unittest` | `runtests('test/')` | 100% pass |
| Schema conformance | `ansatz27` + custom test | Custom test class | All structs validate |
| Dependency direction | Custom script | `grep -r "+skeleton" tissue/` (allowed) and `grep -r "+tissue" skeleton/` (forbidden) | No reverse dependency |

## 8. Implementation Workflow

**Phase template**:

1. **Plan** – Define specification changes (JSON Schema diffs).
2. **Approve** – Human reviews spec delta.
3. **Generate** – AI produces tissue code (function handles or subclasses).
4. **Static gate** – `checkcode` + `miss_hit`.
5. **Test gate** – `matlab.unittest` runs conformance tests.
6. **Dependency gate** – Check skeleton→tissue direction.
7. **Commit** – Update specification, tissue, and `FIXED_PREMISE.md`. Create Git tag.

**Example phase sequence** (game engine):

| Phase | Specification Change | Generated Tissue |
|-------|----------------------|------------------|
| 1 | JSON Schema for `Player` (position, speed) | Function handle `movePlayer` |
| 2 | Schema for `Enemy` (type, spawn pattern) | Subclass of `EnemySkeleton` |
| 3 | Schema for `Stage` (layout, enemy waves) | JSON loader + stage iterator |

## 9. Constraints and Mitigations

| Constraint | Mitigation |
|------------|-------------|
| No static type checking | Runtime validation with `matlab.unittest` + schema checks |
| OOP overhead (100× slower) | Use function handle injection instead of abstract classes for performance‑critical paths |
| No native code generation from JSON Schema | AI generates code; validation gates reject non‑conforming output |
| Dynamic dependencies not detected | Encode all external file names in specification as literals |
| CI license restrictions | Use batch licensing tokens or MATLAB Compiler standalone executables |
| No built‑in fixed premise management | Git tags + `FIXED_PREMISE.md` + custom CI scripts |

## 10. Conclusion

A partial implementation of Deep Coding in MATLAB is feasible for greenfield modules, configuration systems, and Simulink‑based development. The recommended approach uses:

- JSON Schema for structural specification.
- Function handle injection or template method for skeleton‑tissue separation.
- Git tags + `FIXED_PREMISE.md` for recursive refinement.
- `checkcode`, `miss_hit`, and `matlab.unittest` for validation gates.

Performance‑critical numerical code and large legacy scripts are not suitable targets. Start with a pilot module, use the lightweight function handle pattern, and expand only after validation gates are stable.