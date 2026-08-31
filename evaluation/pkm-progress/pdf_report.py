"""Small dependency-free A4 PDF writer for the PKM evidence summary."""

from __future__ import annotations

import textwrap
import unicodedata
from pathlib import Path


PAGE_WIDTH = 595
PAGE_HEIGHT = 842
LEFT = 42
TOP = 800
LINE_HEIGHT = 13
LINES_PER_PAGE = 55


def _pdf_text(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("latin-1", "replace").decode("latin-1")
    return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def _wrap(lines: list[str]) -> list[str]:
    result: list[str] = []
    for line in lines:
        if not line:
            result.append("")
        else:
            result.extend(textwrap.wrap(line, width=96, break_long_words=False, break_on_hyphens=False) or [""])
    return result


def _stream(lines: list[str], page_number: int, total_pages: int) -> bytes:
    commands = ["BT", "/F1 9 Tf", f"{LEFT} {TOP} Td"]
    for line in lines:
        commands.append(f"({_pdf_text(line)}) Tj")
        commands.append(f"0 -{LINE_HEIGHT} Td")
    footer = f"Halaman {page_number}/{total_pages} - Bukti pengujian Gamblock-AI"
    commands.extend(["ET", "BT", "/F1 8 Tf", f"{LEFT} 24 Td", f"({_pdf_text(footer)}) Tj", "ET"])
    return "\n".join(commands).encode("latin-1")


def write_a4_pdf(path: Path, lines: list[str]) -> None:
    """Write plain, searchable Indonesian text as an A4 PDF using a core font."""
    wrapped = _wrap(lines)
    pages = [wrapped[index:index + LINES_PER_PAGE] for index in range(0, len(wrapped), LINES_PER_PAGE)] or [[]]
    # Object 2 is reserved for the page tree because the catalog points to it.
    objects: list[bytes] = [b"<< /Type /Catalog /Pages 2 0 R >>", b""]
    page_ids: list[int] = []
    content_ids: list[int] = []
    for _ in pages:
        page_ids.append(len(objects) + 1)
        objects.append(b"")
        content_ids.append(len(objects) + 1)
        objects.append(b"")
    font_id = len(objects) + 1
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    kids = " ".join(f"{identifier} 0 R" for identifier in page_ids)
    objects[1] = f"<< /Type /Pages /Kids [{kids}] /Count {len(pages)} >>".encode("ascii")
    for index, lines_for_page in enumerate(pages):
        page_id = page_ids[index]
        content_id = content_ids[index]
        objects[page_id - 1] = (
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {PAGE_WIDTH} {PAGE_HEIGHT}] "
            f"/Resources << /Font << /F1 {font_id} 0 R >> >> /Contents {content_id} 0 R >>"
        ).encode("ascii")
        stream = _stream(lines_for_page, index + 1, len(pages))
        objects[content_id - 1] = b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n" + stream + b"\nendstream"
    payload = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for index, obj in enumerate(objects, start=1):
        offsets.append(len(payload))
        payload.extend(f"{index} 0 obj\n".encode("ascii"))
        payload.extend(obj)
        payload.extend(b"\nendobj\n")
    startxref = len(payload)
    payload.extend(f"xref\n0 {len(objects) + 1}\n0000000000 65535 f \n".encode("ascii"))
    for offset in offsets[1:]:
        payload.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    payload.extend(f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{startxref}\n%%EOF\n".encode("ascii"))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
