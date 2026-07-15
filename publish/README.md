# publish — yalix carousel publisher

Compile a yalix Instagram carousel, render Instagram-ready slides, and publish
them as a carousel. Managed with [uv](https://docs.astral.sh/uv/). Run everything
from the **repository root**.

```
uv run publish build <post_dir>            # compile + render slides
uv run publish post  <post_dir>            # build + DRY-RUN publish plan
uv run publish post  <post_dir> --publish  # build + actually upload
```

`<post_dir>` is a post folder, e.g. `Instagram/MatematicasParaML/EspaciosVectoriales`.

## How it works

1. **Compile** — runs `xelatex` **twice** with the post folder as the working
   directory, so the yalix template's relative includes resolve
   (`\yalixroot ../../` → `Instagram/`, plus `Headers/`, `fonts/`,
   `palette.tex`, `veil.png`, `assets/cover.jpg`). This is why the tool does
   **not** copy the lone `.tex` into a temp dir — the includes would break.
2. **Render** — `pdftoppm` rasterises each page straight to a **1080×1350 JPEG**
   (Instagram 4:5). yalix pages are 108×135 mm = exactly 4:5, so no cropping or
   padding is needed. Slides land in `<post_dir>/build/slide-N.jpg` (gitignored).
3. **Publish** — reads `<post_dir>/caption.md` and uploads the ordered slides as
   one carousel via [instagrapi](https://github.com/subzeroid/instagrapi).

## Requirements

- **Build**: `xelatex` (MacTeX/TeX Live) and `pdftoppm` (poppler) on your PATH.
  No Python packages. On macOS: `brew install poppler`. The handwriting font
  **SignPainter** is a macOS system font — building on Linux needs it installed.
- **Publish**: uv resolves the Python deps automatically. The first
  `uv run publish …` creates `.venv` and installs from `pyproject.toml`
  (`uv sync` to do it up front). Then add your credentials:

```bash
cp publish/.env.example .env        # then edit .env with your credentials
```

## Caption

Each post you publish needs a `caption.md` in its folder — written verbatim to
Instagram (Spanish text, CTA, hashtags; max 2200 chars). Copy
`publish/caption.example.md` into the post folder as `caption.md` and edit.

## Publishing safely

`post` is a **dry run by default** — it prints the slide list and caption but
uploads nothing. Add `--publish` to actually post.

instagrapi uses Instagram's **private** API (login with username/password). It
needs no Meta app, but it is against Instagram's ToS and can trigger temporary
blocks. Mitigations baked in: a reused session file
(`publish/.instagram_session.json`), small randomized delays, and low volume.
Keep posting cadence human. If the account is important, consider migrating to
the official Graph API (needs an IG Business/Creator account + Meta app + a host
for the images).

## Secrets

`.env` and `.instagram_session.json` are gitignored — never commit them.
