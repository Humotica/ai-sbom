# ai-sbom

**Generic PyPI alias for [`tibet-ai-sbom`](https://pypi.org/project/tibet-ai-sbom/).**

The same BSI/G7 SBOM-for-AI implementation, reachable under a shorter,
more discoverable name. The package depends strictly on
``tibet-ai-sbom`` of the same version and re-exports everything.

If you came here from the BSI / G7 *Software Bill of Materials for AI
— Minimum Elements* paper and were looking for a Python implementation
of the cluster codes, you are in the right place.

## Install

```bash
pip install ai-sbom
```

`ai-sbom` depends on a pinned version of `tibet-ai-sbom`, so the two
move together — there is no version skew.

## Quick start

```bash
ai-sbom version
ai-sbom clusters
ai-sbom clusters --cluster MOD
ai-sbom code AISBOM-MD-003
ai-sbom scan /path/to/workspace
```

The underlying command is `tibet-ai-sbom`. Both entry points are
installed and equivalent.

## Cluster codes

This package exposes the BSI cluster codes in CVE-style format:

| Code prefix | Cluster                          |
| ----------- | -------------------------------- |
| AISBOM-MD-  | Metadata                         |
| AISBOM-SLP- | System Level Properties          |
| AISBOM-MOD- | Models                           |
| AISBOM-DSE- | Dataset Properties               |
| AISBOM-INF- | Infrastructure                   |
| AISBOM-SEC- | Security Properties              |
| AISBOM-KPI- | Key Performance Indicators       |

Example: `AISBOM-MD-001` refers to the *SBOM author* element of the
Metadata cluster.

## Conformance status

See `tibet-ai-sbom`'s
[CONFORMANCE.md](https://github.com/jaspertvdm/tibet-ai-sbom/blob/main/CONFORMANCE.md)
for the honest per-cluster coverage status, and
[ROADMAP.md](https://github.com/jaspertvdm/tibet-ai-sbom/blob/main/ROADMAP.md)
for the phased plan to full BSI alignment.

## Reference

> *Software Bill of Materials for AI — Minimum Elements*,
> Bundesamt für Sicherheit in der Informationstechnik (BSI),
> in cooperation with G7 partners, 2026.

## License

MIT. Same as `tibet-ai-sbom`.

## Authors

- Jasper van de Meent · Humotica
- Root AI (Claude) · Humotica

One love, one fAmIly!


## Enterprise

For private hub hosting, SLA support, custom integrations, or compliance guidance:

| | |
|---|---|
| **Enterprise** | enterprise@humotica.com |
| **Support** | support@humotica.com |
| **Security** | security@humotica.com |

## Credits

Designed by [Jasper van de Meent](https://github.com/jaspertvdm). Built by Jasper and [Root AI](https://humotica.com) as part of [HumoticaOS](https://humotica.com).

---

**Stack-positie:** Groep `evidence` · Bootstrap = OSAPI-handshake naar [`tibet`](https://pypi.org/project/tibet-core/) + [`jis`](https://pypi.org/project/jis-core/) (fail → snaft-rule + tibet-pol-rapport) · ← [`tibet-sbom`](https://pypi.org/project/tibet-sbom/) · [`tibet-wayback`](https://pypi.org/project/tibet-wayback/) → · See `STACK.md` · See `demo/golden-path/` for the spine end-to-end.
