# GitHub Copilot Instructions for This Repository (Go)

## General goals
- Write clear, idiomatic Go.
- Prefer simplicity and explicitness over clever abstractions.
- Follow existing patterns and conventions already present in this repo.

## Languages and stack
- Language: **Go**.
- Target Go version: see `go.mod` (`go X.Y` line).
- Respect module path and layout defined in `go.mod`.

## Code style
- Follow standard Go idioms as enforced by:
  - `gofmt` / `go fmt`
  - `go vet`
  - Any configured linters (e.g. `golangci-lint`, `staticcheck`).
- Naming:
  - Use short, meaningful names; exported identifiers start with a capital letter.
  - Keep package names short, lower-case, and without underscores.
- Structure:
  - Prefer small, focused functions.
  - Avoid deep inheritance-like patterns; prefer composition.
- Error handling:
  - Return `error` as the last return value.
  - Handle errors explicitly; avoid ignoring them with `_` unless clearly safe.

## Project layout & architecture
- Follow the existing directory layout (e.g. `cmd/`, `internal/`, `pkg/`, `api/`).
- When adding new commands:
  - Place them under `cmd/<appname>/main.go` following the existing pattern.
- When adding internal packages:
  - Place them under `internal/<domain>` or the pattern already used here.
- Reuse existing helper functions and packages instead of duplicating logic.
- Keep packages focused; avoid large “grab bag” utility packages unless the repo already uses that pattern.

## Dependencies
- Use the Go module system (`go.mod`, `go.sum`).
- Prefer standard library packages when reasonable.
- Prefer existing third-party dependencies already present in `go.mod`.
- Do **not** add new external dependencies unless explicitly requested or clearly justified.

## Concurrency
- Use goroutines and channels following existing patterns in this repo.
- Avoid data races; use synchronization primitives from `sync` and `sync/atomic` as needed.
- When in doubt, prefer clarity over “clever” concurrent patterns.

## Logging & configuration
- Use the existing logging approach (e.g. `log`, `zap`, `logrus`, `zerolog`).
- Use the existing configuration mechanism (flags, env vars, config files) instead of introducing a new one.

## Testing
- Use Go’s testing tools:
  - `testing` package.
  - Any additional tools already used (e.g. `testify`, `gomega`, `go-cmp`).
- Place tests in `*_test.go` files in the same package or in a `_test` package, matching current practice.
- For new features and bug fixes:
  - Add or update tests to cover the behavior.
- Use table-driven tests where appropriate, especially for pure functions and logic.

## Documentation & comments
- Add GoDoc-style comments to all exported types, functions, methods, and packages.
- Keep comments concise and focused on *why* something is done, not just *what*.
- Update `README.md` or other docs when user-visible behavior changes.

## APIs & interfaces
- Reuse existing interfaces where possible.
- Avoid over-abstracting; only introduce new interfaces when there are multiple concrete implementations or clear benefits.
- Be careful changing exported APIs; call out any breaking changes explicitly.

## What NOT to do
- Do not change exported function or method signatures without calling this out clearly.
- Do not introduce large new frameworks or libraries without explicit instruction.
- Do not mix unrelated refactors and behavioral changes in a single change.

## When unsure
- Prefer small, incremental changes that match the existing code style.
- When multiple designs are reasonable, outline 2–3 options briefly in comments or in your explanation so the user can choose.
