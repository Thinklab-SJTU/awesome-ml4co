"""
Normalize author strings in papers.csv to: Given-name Family-name, comma-separated (no 'and').
Run: python src/normalize_authors.py  (from repo root)
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "papers.csv"


def clean_token(t: str) -> str:
    """Remove stray sentence-ending period after a single surname (e.g. 'Bengio.' -> 'Bengio')."""
    t = t.strip()
    if len(t) > 1 and t.endswith(".") and " " not in t.rstrip("."):
        return t[:-1].strip()
    return t


def normalize_segment(segment: str) -> str:
    segment = re.sub(r"\s+", " ", segment.strip()).strip('"').strip()
    if not segment:
        return ""
    if segment.lower() == "others":
        return "others"
    if "," not in segment:
        return segment

    parts = [clean_token(p) for p in segment.split(",")]
    parts = [p for p in parts if p]
    parts = [re.sub(r"^and\s+", "", p, flags=re.I) for p in parts]

    if len(parts) >= 2:
        multi = sum(1 for p in parts if len(p.split()) >= 2)
        if multi == len(parts):
            return ", ".join(parts)

    if len(parts) == 2:
        last, first = parts[0], parts[1]
        return f"{first} {last}".strip()

    if len(parts) % 2 == 0:
        names = []
        for i in range(0, len(parts), 2):
            last, first = parts[i], parts[i + 1]
            names.append(f"{first} {last}".strip())
        return ", ".join(names)

    return f"{', '.join(parts[1:])} {parts[0]}".strip()


def normalize_authors_field(s: str) -> str:
    if s is None:
        return ""
    s = str(s).strip()
    if not s:
        return ""

    suffix = ""
    if re.search(r",\s*others\s*$", s, flags=re.I):
        suffix = ", others"
        s = re.sub(r",\s*others\s*$", "", s, flags=re.I).strip()

    s = s.replace(";", ",")
    s = re.sub(r"\s*&\s*", ", ", s)
    s = re.sub(r"\s+", " ", s)

    s = re.sub(r",\s*and\s+", "\x00SEP\x00", s, flags=re.I)
    s = re.sub(r"\s+and\s+", "\x00SEP\x00", s, flags=re.I)

    pieces = [p.strip() for p in s.split("\x00SEP\x00")]
    pieces = [p for p in pieces if p]

    out = [normalize_segment(p) for p in pieces]
    out = [o for o in out if o]
    result = ", ".join(out)
    result = re.sub(r",\s*,", ", ", result)
    result = re.sub(r"\s+", " ", result).strip()
    return result + suffix


def main():
    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)

    if not rows:
        print("empty csv", file=sys.stderr)
        sys.exit(1)

    header = rows[0]
    try:
        ai = header.index("authors")
    except ValueError:
        ai = 6

    for i in range(1, len(rows)):
        if len(rows[i]) > ai:
            rows[i][ai] = normalize_authors_field(rows[i][ai])

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)

    print(f"Updated {len(rows) - 1} data rows in {CSV_PATH}")


if __name__ == "__main__":
    main()
