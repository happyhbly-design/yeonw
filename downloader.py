#!/usr/bin/env python3
"""Simple YouTube downloader CLI using yt-dlp.

Usage:
    python downloader.py "https://www.youtube.com/watch?v=..." -o downloads
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download videos you have rights to using yt-dlp."
    )
    parser.add_argument("url", help="Video URL to download")
    parser.add_argument(
        "-o",
        "--output-dir",
        default="downloads",
        help="Output directory (default: downloads)",
    )
    parser.add_argument(
        "-f",
        "--format",
        default="bestvideo+bestaudio/best",
        help="yt-dlp format selector",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        import yt_dlp
    except ImportError:
        print(
            "yt-dlp가 설치되지 않았습니다. 먼저 `pip install -r requirements.txt`를 실행하세요.",
            file=sys.stderr,
        )
        return 1

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        "format": args.format,
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([args.url])

    print(f"다운로드 완료: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
