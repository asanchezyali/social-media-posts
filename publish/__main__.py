"""CLI for the yalix publishing tool.

    uv run publish build <post_dir>
        Compile the post and render 1080x1350 slides into <post_dir>/build/.

    uv run publish post  <post_dir> [--publish]
        Build, read <post_dir>/caption.md, and publish the carousel.
        DRY RUN by default (prints the plan). Add --publish to actually upload.

Run from the repository root, e.g.

    uv run publish post Instagram/MatematicasParaML/EspaciosVectoriales --publish
"""

from __future__ import annotations

import argparse
from pathlib import Path

from .builder import build_post


def cmd_build(args: argparse.Namespace) -> int:
    build_post(Path(args.post))
    return 0


def cmd_post(args: argparse.Namespace) -> int:
    post_dir = Path(args.post)
    slides = build_post(post_dir)

    caption_file = post_dir / "caption.md"
    if not caption_file.exists():
        raise SystemExit(
            f"Missing {caption_file} — create it with the caption to publish "
            f"(see publish/caption.example.md)."
        )
    caption = caption_file.read_text().strip()

    print("\n" + "=" * 56)
    print(f"POST : {post_dir.name}")
    print(f"SLIDES: {len(slides)}  ", " ".join(s.name for s in slides))
    print(f"CAPTION ({len(caption)} chars):\n")
    print(caption)
    print("=" * 56)

    if not args.publish:
        print("\n🔒 DRY RUN — nothing uploaded. Re-run with --publish to post.")
        return 0

    from .poster import InstagramPoster

    url = InstagramPoster().post_carousel(slides, caption)
    print(f"\n🚀 Published: {url}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="uv run publish", description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("build", help="compile + render slides only")
    b.add_argument("post", help="path to the post folder")
    b.set_defaults(func=cmd_build)

    p = sub.add_parser("post", help="build + publish a carousel (dry-run unless --publish)")
    p.add_argument("post", help="path to the post folder")
    p.add_argument("--publish", action="store_true", help="actually upload to Instagram")
    p.set_defaults(func=cmd_post)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
