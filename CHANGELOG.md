# Changelog

All notable changes to this project will be documented in this file.

This repository follows a candidate-based release flow for early specification development.

---

## [v0.4.0-candidate] - 2026-06-15

### Added

* Added `docs/royalty-os-integration.md`.

  * Defines the v0.4 integration model connecting Compute Access Royalty OS with broader Royalty OS, Trace OS, Communication Royalty OS, and return-flow architectures.
  * Introduces the flow:

    * Origin Contribution
    * Trace Record
    * Attribution Route
    * Allocation Policy
    * Return Flow
    * Compute Access Right
  * Defines origin, trace, attribution, allocation, return-flow, and access-right integration layers.
  * Explains how compute access can become a royalty-style return object.
* Added `schemas/compute-access-royalty-link.schema.json`.

  * Defines the first JSON Schema for linking origin contributions to compute access returns.
  * Supports origin, trace, attribution, allocation, return flow, compute access right reference, review, and audit metadata.
* Added `examples/compute-access-royalty-link.example.yaml`.

  * Provides a valid example of a verified contribution linked to a governed compute access return.
  * Demonstrates Royalty OS-style integration across trace, attribution, allocation, return flow, and access right reference.
* Updated `scripts/validate_examples.py`.

  * Added validation target for `Compute Access Royalty Link`.
  * Now validates:

    * `Compute Access Right`
    * `Contribution to Access Policy`
    * `Multi-Wing Compute Pool`
    * `Compute Access Royalty Link`
* Updated `README.md`.

  * Added v0.4 overview.
  * Added Royalty OS Integration section.
  * Updated repository structure.
  * Updated schemas, examples, validation output, current status, roadmap, and philosophy.

### Validated

* Confirmed that `examples/compute-access-right.example.yaml` validates successfully against `schemas/compute-access-right.schema.json`.
* Confirmed that `examples/contribution-to-access-policy.example.yaml` validates successfully against `schemas/contribution-to-access-policy.schema.json`.
* Confirmed that `examples/multi-wing-compute-pool.example.yaml` validates successfully against `schemas/multi-wing-compute-pool.schema.json`.
* Confirmed that `examples/compute-access-royalty-link.example.yaml` validates successfully against `schemas/compute-access-royalty-link.schema.json`.
* Confirmed that GitHub Actions validation passes with all four schema/example pairs.
* Confirmed that v0.4 is connected to the repository validation loop.

### Design Notes

v0.4 extends the system from access rights, contribution allocation, and shared compute commons into broader Royalty OS integration.

```text
v0.1
Compute Access Right
= the governed access object

v0.2
Contribution-to-Access Allocation
= the policy layer that converts contribution into access return

v0.3
Multi-Wing Compute Commons
= the shared resource layer for governing pooled compute access across multiple wings

v0.4
Royalty OS Integration
= the origin-to-access return bridge connecting trace, attribution, allocation, return flow, and compute access rights
```

The v0.4 model intentionally keeps compute access royalty links:

* origin-aware
* traceable
* attribution-based
* policy-governed
* return-flow aligned
* non-transferable by default
* non-cash by default
* expiring
* reviewable
* auditable
* abuse-resistant

### Release Readiness

`v0.4.0-candidate` is ready to tag once the following files are committed:

```text
README.md
CHANGELOG.md
docs/compute-access-governance.md
docs/contribution-to-access-allocation.md
docs/multi-wing-compute-commons.md
docs/royalty-os-integration.md
schemas/compute-access-right.schema.json
schemas/contribution-to-access-policy.schema.json
schemas/multi-wing-compute-pool.schema.json
schemas/compute-access-royalty-link.schema.json
examples/compute-access-right.example.yaml
examples/contribution-to-access-policy.example.yaml
examples/multi-wing-compute-pool.example.yaml
examples/compute-access-royalty-link.example.yaml
scripts/validate_examples.py
.github/workflows/validate-examples.yml
```

Recommended tag:

```text
v0.4.0-candidate
```

Recommended release title:

```text
v0.4.0-candidate — Royalty OS Integration
```

---

## [v0.3.0-candidate] - 2026-06-15

### Added

* Added `docs/multi-wing-compute-commons.md`.

  * Defines the v0.3 commons model for shared AI compute access governance.
  * Introduces the flow:

    * Shared Compute Pool
    * Wing Contribution
    * Governance Policy
    * Allocation Decision
    * Compute Access Right
    * Usage Trace
    * Review / Adjustment
  * Defines wings, shared compute pools, commons governance layers, allocation modes, anti-abuse design, and review principles.
* Added `schemas/multi-wing-compute-pool.schema.json`.

  * Defines the first JSON Schema for a governed shared compute pool.
  * Supports pool identity, steward, pool type, capacity, eligible wings, allocation policy, usage rules, trace requirements, abuse controls, review configuration, and output expectations.
* Added `examples/multi-wing-compute-pool.example.yaml`.

  * Provides a valid example of an open-source contributor compute pool.
  * Demonstrates multi-wing allocation across Code, Safety, Trace, Education, Governance, and Community Wings.
  * Includes capacity, wing weights, allocation policy, usage rules, trace requirements, abuse controls, and review configuration.
* Updated `scripts/validate_examples.py`.

  * Added validation target for `Multi-Wing Compute Pool`.
  * Now validates:

    * `Compute Access Right`
    * `Contribution to Access Policy`
    * `Multi-Wing Compute Pool`
* Updated `README.md`.

  * Added v0.3 overview.
  * Added Multi-Wing Compute Commons section.
  * Updated repository structure.
  * Updated schemas, examples, validation output, current status, roadmap, and philosophy.

### Validated

* Confirmed that `examples/compute-access-right.example.yaml` validates successfully against `schemas/compute-access-right.schema.json`.
* Confirmed that `examples/contribution-to-access-policy.example.yaml` validates successfully against `schemas/contribution-to-access-policy.schema.json`.
* Confirmed that `examples/multi-wing-compute-pool.example.yaml` validates successfully against `schemas/multi-wing-compute-pool.schema.json`.
* Confirmed that GitHub Actions validation passes with all three schema/example pairs.
* Confirmed that v0.3 is connected to the repository validation loop.

### Design Notes

v0.3 extends the system from individual access rights and contribution-based allocation into shared compute commons.

```text
v0.1
Compute Access Right
= the governed access object

v0.2
Contribution-to-Access Allocation
= the policy layer that converts contribution into access return

v0.3
Multi-Wing Compute Commons
= the shared resource layer for governing pooled compute access across multiple wings
```

### Release

Recommended tag:

```text
v0.3.0-candidate
```

Recommended release title:

```text
v0.3.0-candidate — Multi-Wing Compute Commons
```

---

## [v0.2.0-candidate] - 2026-06-15

### Added

* Added `docs/contribution-to-access-allocation.md`.

  * Defines the v0.2 allocation model for converting useful contributions into governed compute access rights.
  * Introduces the flow:

    * Contribution
    * Trace
    * Evaluation
    * Allocation
    * Compute Access Return
  * Defines contribution types, evaluation principles, allocation levels, policy logic, abuse risks, and return-flow direction.
* Added `schemas/contribution-to-access-policy.schema.json`.

  * Defines the first JSON Schema for contribution-to-access allocation policy.
  * Supports eligible contribution types, evaluation criteria, allocation levels, access right mapping, expiration rules, balance rules, review requirements, abuse controls, and trace requirements.
* Added `examples/contribution-to-access-policy.example.yaml`.

  * Provides a valid example policy for converting verified contributions into non-transferable, expiring, auditable compute access rights.
  * Demonstrates contribution evaluation and access right mapping across allocation levels.
* Updated `scripts/validate_examples.py`.

  * Added validation target for `Contribution to Access Policy`.
  * Now validates both:

    * `Compute Access Right`
    * `Contribution to Access Policy`
* Updated `README.md`.

  * Added v0.2 overview.
  * Added Contribution-to-Access Allocation section.
  * Updated repository structure.
  * Updated schemas, examples, validation output, current status, and roadmap.

### Validated

* Confirmed that `examples/compute-access-right.example.yaml` validates successfully against `schemas/compute-access-right.schema.json`.
* Confirmed that `examples/contribution-to-access-policy.example.yaml` validates successfully against `schemas/contribution-to-access-policy.schema.json`.
* Confirmed that GitHub Actions validation passes with both schema/example pairs.
* Confirmed that v0.2 is connected to the repository validation loop.

### Design Notes

v0.2 extends v0.1 from access-right definition into contribution-based allocation.

```text
v0.1
Compute Access Right
= the governed access object

v0.2
Contribution-to-Access Allocation
= the policy layer that converts contribution into access return
```

### Release

Recommended tag:

```text
v0.2.0-candidate
```

Recommended release title:

```text
v0.2.0-candidate — Contribution-to-Access Allocation
```

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

v0.1 intentionally treats compute access rights as:

* non-transferable
* non-cash
* scoped
* expiring
* traceable
* reviewable

v0.1 does **not** define:

* financial tokenization
* resale markets
* speculative assets
* transferable access tokens
* automated royalty payment rails
* cross-platform exchange protocols

### Release

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

### v0.5 — Sovereign / Space Compute Access Protocol

Planned direction:

* sovereign compute governance
* space or off-grid compute infrastructure
* jurisdictional stewardship
* AI compute access rights across infrastructure domains
* human review and commons protection
* compute access return across sovereign or orbital infrastructure

Potential files:

```text
docs/sovereign-compute-access-protocol.md
schemas/sovereign-compute-access.schema.json
examples/sovereign-compute-access.example.yaml
```

