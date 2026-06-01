"""
ai-sbom — generic alias for tibet-ai-sbom.

This package is intentionally a thin alias around ``tibet-ai-sbom`` so
that engineers and auditors who type ``pip install ai-sbom`` reach the
same BSI/G7 SBOM-for-AI implementation as the canonical
``tibet-ai-sbom`` package.

The version of ``ai-sbom`` is held in lock-step with the version of
``tibet-ai-sbom`` it depends on. Bumping one always bumps the other.

Everything below re-exports the underlying ``tibet_ai_sbom`` module.
"""
from __future__ import annotations

from tibet_ai_sbom import (
    __version__ as _tibet_ai_sbom_version,
    BSICluster,
    CLUSTER_CODES,
    cluster_for_code,
    list_cluster_codes,
)

__version__ = _tibet_ai_sbom_version
__author__ = "Jasper van de Meent & Root AI (Claude)"

__all__ = [
    "__version__",
    "BSICluster",
    "CLUSTER_CODES",
    "cluster_for_code",
    "list_cluster_codes",
]
