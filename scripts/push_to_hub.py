#!/usr/bin/env python3
"""Upload the dataset to the Hugging Face Hub.

Example:
    python scripts/push_to_hub.py --repo-id your-username/ramanujan-formulae
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from ramanujan_dataset import to_hf_dataset


def main() -> int:
    parser = argparse.ArgumentParser(description="Push Ramanujan dataset to Hugging Face Hub")
    parser.add_argument("--repo-id", required=True, help="Target dataset repo, e.g. user/ramanujan-formulae")
    parser.add_argument("--private", action="store_true", help="Create or update a private dataset")
    args = parser.parse_args()

    dataset = to_hf_dataset()
    dataset.push_to_hub(args.repo_id, private=args.private)
    print(f"Pushed dataset to https://huggingface.co/datasets/{args.repo_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
