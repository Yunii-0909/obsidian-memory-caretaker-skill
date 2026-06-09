#!/usr/bin/env python3
import argparse
import os
import re
from pathlib import Path

DEFAULT_VAULT = Path(os.environ.get("OBSIDIAN_VAULT_PATH", "")).expanduser()


def normalize_terms(query: str):
    parts = re.split(r"[\s,，、|/]+", query.strip())
    return [p for p in parts if p]


def score_text(text: str, terms):
    lowered = text.lower()
    score = 0
    hits = []
    for term in terms:
        n = lowered.count(term.lower())
        if n:
            score += n
            hits.append(term)
    return score, hits


def snippet(text: str, terms, width=90):
    lowered = text.lower()
    positions = [lowered.find(t.lower()) for t in terms if lowered.find(t.lower()) >= 0]
    if not positions:
        return ""
    start = max(0, min(positions) - 35)
    end = min(len(text), start + width)
    return re.sub(r"\s+", " ", text[start:end]).strip()


def main():
    parser = argparse.ArgumentParser(description="Search Elora's Obsidian vault for relevant memory notes.")
    parser.add_argument("query", help="Search terms, e.g. '保研 周报 suki'")
    parser.add_argument("--vault", default=str(DEFAULT_VAULT) if str(DEFAULT_VAULT) != "." else "", help="Obsidian vault path; defaults to $OBSIDIAN_VAULT_PATH")
    parser.add_argument("--limit", type=int, default=12, help="Maximum results")
    args = parser.parse_args()

    if not args.vault:
        raise SystemExit("Vault path not set. Set OBSIDIAN_VAULT_PATH or pass --vault /path/to/vault.")
    vault = Path(os.path.expanduser(args.vault))
    terms = normalize_terms(args.query)
    if not terms:
        raise SystemExit("No search terms provided.")
    if not vault.exists():
        raise SystemExit(f"Vault not found: {vault}")

    results = []
    for path in vault.rglob("*.md"):
        if any(part.startswith(".") for part in path.relative_to(vault).parts):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        score, hits = score_text(text + "\n" + path.name, terms)
        if score:
            results.append((score, path, hits, snippet(text, terms)))

    results.sort(key=lambda x: (-x[0], str(x[1])))
    for score, path, hits, snip in results[: args.limit]:
        rel = path.relative_to(vault)
        print(f"{score:>3}  {rel}  hits={','.join(sorted(set(hits)))}")
        if snip:
            print(f"     {snip}")


if __name__ == "__main__":
    main()
