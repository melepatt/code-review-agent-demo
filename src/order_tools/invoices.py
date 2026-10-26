"""Invoice document access helpers."""

from pathlib import Path


def read_invoice(root: Path, invoice_id: str) -> str:
    """Read the requested invoice document from the invoice root."""
    path = root / f"{invoice_id}.txt"
    return path.read_text(encoding="utf-8")
