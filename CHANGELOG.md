# Changelog — ai-sbom

All notable changes to this alias package will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.1] — 2026-05-16

### Changed

- Upstream pin updated: `tibet-ai-sbom>=0.2.0,<0.3` (was `==0.1.0`)
  - Picks up cap-bus gateway-ingest, coffee-lane field projection,
    actor/provider surface views, and governance-conclusion alignment.
- No code changes in this package — purely a pin refresh.

---

## [0.1.0] — 2026-05-15

### Added

- Initial alias-package release.
- Re-exports `tibet-ai-sbom` cluster codes and CLI under the generic
  `ai-sbom` name.
- Pinned to `tibet-ai-sbom==0.1.0`.
- Entry-point: `ai-sbom` → `ai_sbom.cli:main`.
