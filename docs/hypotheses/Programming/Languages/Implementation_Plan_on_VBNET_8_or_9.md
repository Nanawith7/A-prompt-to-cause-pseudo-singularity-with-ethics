---
title: "Implementation Plan on VBNET 8 or 9"
description: "A structured implementation plan for applying Deep Coding methodology to Visual Basic .NET 8 and 9, covering structural specification, skeleton–tissue separation, generative conformance, validation gates, recursive refinement with fixed premises, and CI/CD automation."
author: "Nanawith7"
layout: default
categories: ["Software Engineering", ".NET", "VB.NET", "AI-Assisted Development"]
tags: ["deep_coding", "VB.NET", "NSwag", "NDepend", "Partial_Classes", "Template_Method", "static_analysis", "Git_Worktree", "CI/CD"]
---

# Implementation Plan on VBNET 8 or 9

## 1. Core Mapping to VB.NET 8/9 Features

| Principle | VB.NET Implementation | Tooling / Syntax |
|-----------|----------------------|------------------|
| Structural specification | OpenAPI / JSON Schema | NSwag, YAML |
| Skeleton (invariant) | `MustInherit` class + `NotOverridable` template method | VB.NET 8/9 |
| Tissue (generated) | `Inherits` + `Overrides` concrete class | NSwag generation |
| Physical separation | `Partial` class across multiple files | Language built-in |
| Hook injection | `Partial Private Sub` (zero-cost if not implemented) | Language built-in |
| Interface contract | `Interface` + `Implements` | Language built-in |
| Compile-time validation | Custom Roslyn analyzer | Roslyn API (C# written, targets VB.NET) |
| Architecture validation | NDepend with CQLinq rules | NDepend, `CodeRuleAttribute` |
| Incremental rebuild | MSBuild `Inputs`/`Outputs` attributes | MSBuild |
| API compatibility | NDepend baseline comparison | NDepend GitHub Action |
| Phase immutability | Git annotated tags | `git tag -a phase-N-complete` |
| Parallel phases | Git worktree | `git worktree add` |
| CI/CD pipeline | GitHub Actions on `windows-latest` | NSwag + NDepend + dotnet |

## 2. Structural Specification Layer

Define all public contracts in OpenAPI YAML.  
Example `spec.yaml`:

```yaml
openapi: 3.0.3
paths:
  /validate/email:
    post:
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                email:
                  type: string
                  pattern: '^[^\s@]+@([^\s@]+\.)+[^\s@]+$'
```

NSwag configuration (`nswag.json`):

```json
{
  "runtime": "Net80",
  "documentGenerator": {
    "fromDocument": {
      "url": "spec.yaml"
    }
  },
  "codeGenerators": {
    "openApiToCSharpClient": {
      "output": "Generated/ApiClient.vb",
      "generateClientInterfaces": true
    }
  }
}
```

Run generation: `nswag run nswag.json`

## 3. Skeleton (Invariant Layer)

Create abstract base class with template method pattern.

```vb.net
' Skeleton/ValidatorBase.vb
Public MustInherit Class ValidatorBase(Of TRequest)
    Implements IValidator(Of TRequest)

    Partial Private Sub OnBeforeValidate(request As TRequest)
    End Sub

    Partial Private Sub OnAfterValidate(request As TRequest, result As Boolean)
    End Sub

    Public NotOverridable Async Function ValidateAsync(
        request As TRequest,
        Optional token As CancellationToken = Nothing
    ) As Task(Of Boolean) Implements IValidator(Of TRequest).ValidateAsync

        OnBeforeValidate(request)
        Dim result = Await ExecuteCoreAsync(request, token)
        OnAfterValidate(request, result)
        Return result
    End Function

    Protected MustOverride Function ExecuteCoreAsync(
        request As TRequest,
        token As CancellationToken
    ) As Task(Of Boolean)
End Class
```

Interface defines contract:

```vb.net
' Skeleton/IValidator.vb
Public Interface IValidator(Of T)
    Function ValidateAsync(request As T, token As CancellationToken) As Task(Of Boolean)
End Interface
```

## 4. Tissue (Generated Layer)

NSwag produces concrete implementation inheriting from skeleton.

```vb.net
' Generated/EmailValidator.vb (auto-generated, do not edit)
Partial Public Class EmailValidator
    Inherits ValidatorBase(Of EmailRequest)

    Protected Overrides Async Function ExecuteCoreAsync(
        request As EmailRequest,
        token As CancellationToken
    ) As Task(Of Boolean)
        Dim pattern = "^[^\s@]+@([^\s@]+\.)+[^\s@]+$"
        Return Regex.IsMatch(request.Email, pattern)
    End Function
End Class
```

## 5. Manual Extension Layer

Developers add custom logic in separate partial file.

```vb.net
' Custom/EmailValidator.Custom.vb
Partial Public Class EmailValidator
    Private Sub OnBeforeValidate(request As EmailRequest)
        Log($"Validating: {request.Email}")
    End Sub

    Private Sub OnAfterValidate(request As EmailRequest, result As Boolean)
        If result Then Cache(request.Email)
    End Sub

    Private Sub Log(message As String) ' implementation
    Private Sub Cache(email As String) ' implementation
End Class
```

## 6. Validation Gates

### 6.1 Compile-Time (Roslyn Analyzer)

Create a Roslyn analyzer (in C#) that targets VB.NET syntax.  
Enforce rule: Types in `Tissue` namespace must inherit from `Skeleton.ValidatorBase`.

### 6.2 Architecture Tests (NDepend)

Write CQLinq rule inside VB.NET source file using `CodeRuleAttribute`:

```vb.net
<CodeRuleAttribute("Tissue must only depend on Skeleton")>
Public Module ArchitectureRules
    Public Function TissueOnlyDependsOnSkeleton() As ICodeRuleResult
        ' CQLinq query embedded
    End Function
End Module
```

### 6.3 Generated Code Verification

In CI pipeline:

```bash
git diff --exit-code -- '**/*.vb'
```

## 7. Recursive Refinement with Fixed Premises

Workflow per phase:

1. Checkout latest phase tag: `git checkout phase-N-complete`
2. Create branch: `git checkout -b phase-N+1`
3. Update structural specification (`spec.yaml`)
4. Regenerate tissue: `nswag run nswag.json`
5. Run validation gates (see Section 6)
6. Commit changes
7. Tag completion: `git tag -a phase-(N+1)-complete -m "Phase N+1 complete"`

Parallel phase development using worktrees:

```bash
git worktree add ../project-phase2 phase2-branch
git worktree add ../project-phase3 phase3-branch
```

## 8. CI/CD Pipeline (GitHub Actions)

```yaml
name: Deep Coding Validation

on: [push, pull_request]

jobs:
  validate:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup .NET 8
        uses: actions/setup-dotnet@v4
        with:
          dotnet-version: '8.0.x'

      - name: Restore tools
        run: dotnet tool restore

      - name: Generate from OpenAPI
        run: nswag run nswag.json

      - name: Verify generated code is committed
        run: git diff --exit-code -- '**/*.vb'

      - name: Build
        run: dotnet build --configuration Release

      - name: NDepend analysis
        uses: ndepend/ndepend-action@v1
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          license: ${{ secrets.NDEPEND_LICENSE }}

      - name: Test
        run: dotnet test --configuration Release --no-build
```

## 9. Phase Transition Checklist

| Step | Action | Verification |
|------|--------|--------------|
| 1 | Update OpenAPI spec | Manual review |
| 2 | Regenerate VB.NET client | NSwag exit code 0 |
| 3 | Check generated code diff | `git diff` shows only expected changes |
| 4 | Run Roslyn analyzers | Build succeeds with no warnings |
| 5 | Run NDepend rules | Quality gate passes |
| 6 | Execute unit tests | All tests pass |
| 7 | Commit and tag | Tag pushed to remote |

## 10. Constraints and Built-in Workarounds

| Constraint | Workaround |
|------------|------------|
| Partial method cannot return value | Use `Overridable` function for return-needed hooks |
| Partial method is `Private` only | Acceptable for internal skeleton hooks |
| NSwag configuration complexity | Store template `nswag.json` in repository root |
| NDepend requires commercial license | For open-source, use Visual Studio layer diagrams or custom Roslyn analyzer |
| Incrementalist does not support VB.NET | Use MSBuild `Inputs`/`Outputs` attributes |
| ApiCompat for VB.NET untested | Use NDepend baseline comparison instead |

## 11. Expected Outcomes

- First generated implementation satisfies structural specification by construction
- Skeleton remains invariant across phases
- Tissue regenerated from updated specification without manual propagation
- Architecture violations cause CI build failure
- Each phase tag allows safe rollback
- Context cost remains independent of codebase size