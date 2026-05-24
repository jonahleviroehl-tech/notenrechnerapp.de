"""Generates a printable Notenschlüssel-Übersicht PDF.

Output: website/assets/notenschluessel-uebersicht.pdf

The PDF mirrors the three preset thresholds from notenschluessel-rechner/index.html
(50/45/40% Bestehensgrenze). Single A4 page, three columns side-by-side, ready to
print and pin on a desk.

Requires: reportlab (pip install reportlab)

Usage: python3 _build/gen_notenschluessel_pdfs.py
"""
from pathlib import Path
from datetime import date

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "notenschluessel-uebersicht.pdf"

# Mirror PRESETS in notenschluessel-rechner/index.html — keep IN SYNC.
PRESETS = {
    "50": [
        (15, 98), (14, 95), (13, 92), (12, 88), (11, 85), (10, 81),
        (9, 76), (8, 72), (7, 67), (6, 61), (5, 56), (4, 50),
        (3, 43), (2, 37), (1, 30), (0, 0),
    ],
    "45": [
        (15, 98), (14, 94), (13, 90), (12, 85), (11, 80), (10, 75),
        (9, 70), (8, 65), (7, 60), (6, 55), (5, 50), (4, 45),
        (3, 39), (2, 32), (1, 24), (0, 0),
    ],
    "40": [
        (15, 95), (14, 90), (13, 85), (12, 80), (11, 75), (10, 70),
        (9, 65), (8, 60), (7, 55), (6, 50), (5, 45), (4, 40),
        (3, 33), (2, 27), (1, 20), (0, 0),
    ],
}

NP_MAP = {
    15: "1+", 14: "1", 13: "1−", 12: "2+", 11: "2", 10: "2−",
    9: "3+", 8: "3", 7: "3−", 6: "4+", 5: "4", 4: "4−",
    3: "5+", 2: "5", 1: "5−", 0: "6",
}

# Brand colors (mirror site CSS).
PRIMARY = HexColor("#2F60C0")
PRIMARY_DARK = HexColor("#1F4A9C")
TEXT = HexColor("#0F0F10")
TEXT_SECONDARY = HexColor("#3B3B3F")
TEXT_MUTED = HexColor("#6E6E73")
BORDER = HexColor("#E8E6E1")
BG_SUBTLE = HexColor("#F7F6F3")
GRADE_1 = HexColor("#15803D")
GRADE_2 = HexColor("#4D7C0F")
GRADE_3 = HexColor("#A16207")
GRADE_4 = HexColor("#C2410C")
GRADE_5 = HexColor("#B91C1C")


def grade_color(np: int):
    if np >= 13: return GRADE_1
    if np >= 10: return GRADE_2
    if np >= 7:  return GRADE_3
    if np >= 4:  return GRADE_4
    return GRADE_5


def grade_bg(np: int):
    # Light tinted background per grade band.
    if np >= 13: return HexColor("#E6F2EA")
    if np >= 10: return HexColor("#EFF1E2")
    if np >= 7:  return HexColor("#F8EFE0")
    if np >= 4:  return HexColor("#FAEADD")
    return HexColor("#F7E6E6")


def draw_header(c, page_width, page_height):
    margin = 18 * mm
    # Brand mark — solid square + wordmark, no logo asset dependency.
    c.setFillColor(PRIMARY)
    c.roundRect(margin, page_height - margin - 9 * mm, 9 * mm, 9 * mm, 2 * mm, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(margin + 4.5 * mm, page_height - margin - 6 * mm, "N")

    c.setFillColor(TEXT)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin + 12 * mm, page_height - margin - 4.2 * mm,
                 "Der Notenrechner")
    c.setFillColor(TEXT_MUTED)
    c.setFont("Helvetica", 9)
    c.drawString(margin + 12 * mm, page_height - margin - 8.2 * mm,
                 "notenrechnerapp.de")

    # Right-side date.
    c.setFillColor(TEXT_MUTED)
    c.setFont("Helvetica", 9)
    today = date.today().strftime("%d.%m.%Y")
    c.drawRightString(page_width - margin, page_height - margin - 4.2 * mm,
                      f"Stand: {today}")
    c.drawRightString(page_width - margin, page_height - margin - 8.2 * mm,
                      "Kostenlos · ohne Tracking")


def draw_title(c, page_width, y):
    margin = 18 * mm
    c.setFillColor(TEXT)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(margin, y, "Notenschlüssel-Übersicht")
    c.setFillColor(TEXT_SECONDARY)
    c.setFont("Helvetica", 10.5)
    c.drawString(
        margin, y - 6 * mm,
        "Drei gängige Notenschlüssel im Vergleich — die Spalte zeigt die Mindestprozente"
    )
    c.drawString(
        margin, y - 10.5 * mm,
        "für jede Notenpunktzahl. Bestanden ab Note 4 (5 Notenpunkte)."
    )


def draw_column(c, x, y_top, col_width, preset_key, accent_label):
    """Draw one Notenschlüssel column with header card + table."""
    thresholds = PRESETS[preset_key]
    row_height = 7.2 * mm
    header_height = 11 * mm

    # Column header band.
    c.setFillColor(PRIMARY)
    c.roundRect(x, y_top - header_height, col_width, header_height, 2 * mm,
                fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(x + col_width / 2, y_top - 5 * mm,
                        f"{preset_key}-%-Schlüssel")
    c.setFont("Helvetica", 8.5)
    c.drawCentredString(x + col_width / 2, y_top - 9 * mm, accent_label)

    # Table header row.
    table_y = y_top - header_height - 1 * mm
    c.setFillColor(BG_SUBTLE)
    c.rect(x, table_y - 5 * mm, col_width, 5 * mm, fill=1, stroke=0)
    c.setFillColor(TEXT_MUTED)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(x + 3 * mm, table_y - 3.4 * mm, "NP")
    c.drawString(x + 11 * mm, table_y - 3.4 * mm, "NOTE")
    c.drawRightString(x + col_width - 3 * mm, table_y - 3.4 * mm,
                      "MIND. %")

    # Rows.
    cursor_y = table_y - 5 * mm
    for np, min_pct in thresholds:
        cursor_y -= row_height
        # Alternating subtle background for legibility.
        if np % 2 == 0:
            c.setFillColor(HexColor("#FBFAF6"))
            c.rect(x, cursor_y, col_width, row_height, fill=1, stroke=0)

        # Grade-color dot.
        c.setFillColor(grade_color(np))
        c.circle(x + 4 * mm, cursor_y + row_height / 2, 1.6 * mm, fill=1, stroke=0)

        # NP value.
        c.setFillColor(TEXT)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(x + 7.2 * mm, cursor_y + row_height / 2 - 1.1 * mm, str(np))

        # Traditional note.
        c.setFillColor(TEXT_SECONDARY)
        c.setFont("Helvetica", 9.5)
        c.drawString(x + 13 * mm, cursor_y + row_height / 2 - 1.1 * mm,
                     NP_MAP[np])

        # Mind. %.
        c.setFillColor(TEXT)
        c.setFont("Helvetica-Bold", 9.5)
        pct_label = f"{min_pct} %" if np > 0 else "0 %"
        c.drawRightString(x + col_width - 3 * mm,
                          cursor_y + row_height / 2 - 1.1 * mm, pct_label)

    # Outer border.
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.6)
    c.rect(x, cursor_y, col_width, (y_top - cursor_y), fill=0, stroke=1)


def draw_footer(c, page_width):
    margin = 18 * mm
    c.setFillColor(TEXT_MUTED)
    c.setFont("Helvetica", 8)
    c.drawString(margin, 14 * mm,
                 "Punkte = (Mindestprozent / 100) × Maximalpunktzahl. Beispiel: 80 % von "
                 "60 Punkten = 48 Punkte.")
    c.drawString(margin, 10 * mm,
                 "Online-Rechner und App (iPhone, iPad, Android in Kürze) auf "
                 "notenrechnerapp.de/notenschluessel-rechner/")


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    page_width, page_height = A4

    c = canvas.Canvas(str(OUT), pagesize=A4)
    c.setTitle("Notenschlüssel-Übersicht")
    c.setAuthor("Der Notenrechner — notenrechnerapp.de")
    c.setSubject("Notenschlüssel 50%, 45%, 40% — Mindestprozente für die Notenpunkte 15 bis 0")
    c.setKeywords("Notenschlüssel, Notenpunkte, Oberstufe, Lehrkräfte, Klausur")

    draw_header(c, page_width, page_height)
    draw_title(c, page_width, page_height - 36 * mm)

    # Three columns starting below title block.
    margin = 18 * mm
    inner_width = page_width - 2 * margin
    gutter = 6 * mm
    col_width = (inner_width - 2 * gutter) / 3
    columns_top = page_height - 55 * mm

    draw_column(c, margin, columns_top, col_width, "50",
                "Hohe Bestehensgrenze · Oberstufe")
    draw_column(c, margin + col_width + gutter, columns_top, col_width, "45",
                "Mittlere Bestehensgrenze")
    draw_column(c, margin + 2 * (col_width + gutter), columns_top, col_width, "40",
                "Niedrige Bestehensgrenze")

    draw_footer(c, page_width)

    c.showPage()
    c.save()
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
