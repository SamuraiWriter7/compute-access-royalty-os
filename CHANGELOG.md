# Changelog

All notable changes to this project will be documented in this file.

This repository follows a candidate-based release flow for early specification development.

---

## [v0.1.0-candidate] - 2026-06-15

### Added

* Added the initial **Compute Access Royalty OS** repository structure.
* Added `docs/compute-access-governance.md`.

  * Defines the conceptual model for governing AI compute access rights.
  * Introduces permission, trace, allocation, lifecycle, review, and return-flow layers.
  * Establishes compute access as a governed, scoped, expiring, and reviewable resource.
* Added `schemas/compute-access-right.schema.json`.

  * Defines the first JSON Schema for a compute access right.
  * Supports rate-limit resets, priority usage windows, temporary access boosts, model access credits, agent execution allowances, contributor access grants, and community pool grants.
  * Includes trigger, scope, lifecycle, policy, trace, review, and return-flow metadata.
* Added `examples/compute-access-right.example.yaml`.

  * Provides a valid example of a contribution-based compute access return.
  * Demonstrates a non-transferable, non-cash, expiring rate-limit reset with audit trace.
* Added `scripts/validate_examples.py`.

  * Validates YAML examples against JSON Schemas.
  * Uses `jsonschema` Draft 2020-12 validation.
  * Includes readable validation output and error paths.
* Added `.github/workflows/validate-examples.yml`.

  * Runs example validation on push, pull request, and manual workflow dispatch.
* Added `README.md`.

  * Explains repository purpose, structure, validation workflow, v0.1 scope, roadmap, and design principles.

### Validated

* Confirmed that `examples/compute-access-right.example.yaml` validates successfully against `schemas/compute-access-right.schema.json`.
* Confirmed that GitHub Actions validation passes.
* Confirmed the repository has a working v0.1 validation loop.

### Fixed During Candidate Preparation

* Fixed GitHub Actions workflow nesting.

  * `steps:` must be nested under `jobs.<job_id>`.
* Fixed Python root path resolution.

  * Replaced corrupted file reference with `Path(__file__).resolve().parents[1]`.
* Fixed YAML root nesting.

  * Ensured all fields are correctly nested under `compute_access_right`.
* Confirmed the example is parsed as an object rather than `null`.

### Design Notes

* v0.1 intentionally treats compute access rights as:

  * non-transferable
  * non-cash
  * scoped
  * expiring
  * traceable
  * reviewable
* v0.1 does **not** define:

  * financial tokenization
  * resale markets
  * speculative assets
  * transferable access tokens
  * automated royalty payment rails
  * cross-platform exchange protocols

### Release Readiness

`v0.1.0-candidate` is ready to tag once the following files are committed:

```text
README.md
CHANGELOG.md
docs/compute-access-governance.md
schemas/compute-access-right.schema.json
examples/compute-access-right.example.yaml
scripts/validate_examples.py
.github/workflows/validate-examples.yml
```

Recommended tag:

```text
v0.1.0-candidate
```

Recommended release title:

```text
v0.1.0-candidate — Compute Access Right Governance Foundation
```

---

## Planned

### v0.2 — Contribution-to-Access Allocation

Planned direction:

* contribution scoring
* contribution-to-access policy
* verified contribution records
* access allocation rules
* review boundaries
* return-flow evaluation

Potential files:

```text
docs/contribution-to-access-allocation.md
schemas/contribution-to-access-policy.schema.json
examples/contribution-to-access-policy.example.yaml
```

### v0.3 — Multi-Wing Compute Commons

Planned direction:

* shared compute pools
* multi-wing access governance
* community allocation
* cross-agent compute coordination
* abuse-resistant compute commons

Potential files:

```text
docs/multi-wing-compute-commons.md
schemas/multi-wing-compute-pool.schema.json
examples/multi-wing-compute-pool.example.yaml
```
