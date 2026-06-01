"""
ai-sbom CLI — generic alias that delegates to ``tibet-ai-sbom``.

Running ``ai-sbom version`` is equivalent to ``tibet-ai-sbom version``;
the underlying implementation is the same.
"""
from __future__ import annotations

from tibet_ai_sbom.cli import main as _tibet_main


def main(argv: list[str] | None = None) -> int:
    return _tibet_main(argv)


if __name__ == "__main__":
    import sys
    sys.exit(main())
