"""Compile a yalix carousel post and render Instagram-ready slides.

The build has NO Python package dependencies: it shells out to `xelatex`
(the yalix template needs XeLaTeX + fontspec, not pdflatex) and `pdftoppm`
(poppler). A post is compiled *in its own directory* so the template's
relative includes resolve — `\\yalixroot ../../` -> Instagram/, plus
Headers/, fonts/, palette.tex, veil.png and assets/cover.jpg.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

# Instagram recommended portrait size (4:5). yalix pages are 108x135 mm,
# i.e. exactly 4:5, so forcing both dimensions rescales without distortion.
IG_WIDTH, IG_HEIGHT = 1080, 1350

# LaTeX build litter to remove after a successful compile (the .pdf stays).
AUX_EXTS = (".aux", ".log", ".out", ".synctex.gz", ".nav", ".snm", ".toc")


def find_tex(post_dir: Path) -> Path:
    """Locate a post's main .tex — `<Folder>/<Folder>.tex`, else the sole .tex."""
    named = post_dir / f"{post_dir.name}.tex"
    if named.exists():
        return named
    texs = sorted(post_dir.glob("*.tex"))
    if len(texs) == 1:
        return texs[0]
    raise SystemExit(
        f"Could not pick a .tex in {post_dir} "
        f"(expected {post_dir.name}.tex or exactly one .tex, found {len(texs)})"
    )


def compile_post(post_dir: Path, tex: Path) -> Path:
    """Run XeLaTeX twice (page counter + overlays need two passes)."""
    print(f"🧬 xelatex {tex.name} (2 passes)…")
    result = None
    for _ in range(2):
        result = subprocess.run(
            ["xelatex", "-interaction=nonstopmode", tex.name],
            cwd=post_dir,
            capture_output=True,
            text=True,
        )
    pdf = post_dir / f"{tex.stem}.pdf"
    if not pdf.exists():
        if result is not None:
            sys.stderr.write(result.stdout[-3000:])
        raise SystemExit(f"🛑 xelatex did not produce {pdf.name}")
    print(f"📄 compiled → {pdf.name}")
    return pdf


def render(pdf: Path, out_dir: Path) -> list[Path]:
    """Render every PDF page straight to a 1080x1350 JPEG with pdftoppm."""
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    print("🧪 pdftoppm → JPEG slides…")
    subprocess.run(
        [
            "pdftoppm", "-jpeg", "-jpegopt", "quality=95",
            "-scale-to-x", str(IG_WIDTH), "-scale-to-y", str(IG_HEIGHT),
            str(pdf), str(out_dir / "slide"),
        ],
        check=True,
    )
    slides = sorted(out_dir.glob("slide-*.jpg"), key=_page_num)
    if not slides:
        raise SystemExit(f"🛑 pdftoppm produced no slides in {out_dir}")
    return slides


def _page_num(p: Path) -> int:
    try:
        return int(p.stem.split("-")[-1])
    except ValueError:
        return 1 << 30


def clean_aux(post_dir: Path, stem: str) -> None:
    for ext in AUX_EXTS:
        f = post_dir / f"{stem}{ext}"
        if f.exists():
            f.unlink()


def build_post(post_dir: Path) -> list[Path]:
    """Compile + render a post. Returns the ordered slide JPEG paths."""
    post_dir = Path(post_dir).resolve()
    if not post_dir.is_dir():
        raise SystemExit(f"Not a directory: {post_dir}")
    tex = find_tex(post_dir)
    pdf = compile_post(post_dir, tex)
    slides = render(pdf, post_dir / "build")
    clean_aux(post_dir, tex.stem)
    print(f"✅ {len(slides)} slide(s) → {post_dir / 'build'}")
    return slides
