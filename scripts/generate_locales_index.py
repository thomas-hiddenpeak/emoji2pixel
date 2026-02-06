#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES_DIR = ROOT / "locales"
INDEX_FILE = LOCALES_DIR / "index.json"


def main():
    if not LOCALES_DIR.exists():
        raise SystemExit("locales directory not found")

    locales = []
    for path in sorted(LOCALES_DIR.glob("*.json")):
        if path.name == "index.json":
            continue
        locales.append(path.stem)

    INDEX_FILE.write_text(json.dumps(locales, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {INDEX_FILE} with {len(locales)} locale(s)")


if __name__ == "__main__":
    main()
