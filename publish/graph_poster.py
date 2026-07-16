"""Publish a carousel via the OFFICIAL Instagram Graph API (Content Publishing).

This is the ToS-compliant path and does not fight Instagram's anti-bot
checkpoints the way the private API (instagrapi) does. It requires a one-time
Meta setup — see publish/GRAPH_API.md — which yields two secrets in .env:

    IG_USER_ID        the Instagram *Business/Creator* account id
    IG_ACCESS_TOKEN   a long-lived token with `instagram_content_publish`

Publishing flow (per the Graph API docs):
    1. The API fetches each image from a PUBLIC https URL, so we first upload
       every slide to a host and collect its URL (default: catbox.moe; or set
       IMAGE_BASE_URL to serve them yourself, e.g. raw.githubusercontent.com).
    2. Create one child container per image  (is_carousel_item=true).
    3. Create the CAROUSEL container with the children + caption.
    4. Poll the container until status_code == FINISHED.
    5. media_publish the carousel.
"""

from __future__ import annotations

import logging
import os
import time
from pathlib import Path

import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("publish.graph")

CATBOX = "https://catbox.moe/user/api.php"

# Two Instagram publishing products, same endpoints/params, different host:
#   - "Instagram API with Instagram Login"  → https://graph.instagram.com  (no FB Page)
#   - "Instagram Graph API" (Facebook Login) → https://graph.facebook.com  (needs FB Page)
# Default to the Instagram-Login host; override with GRAPH_BASE_URL if needed.
DEFAULT_BASE = "https://graph.instagram.com/v21.0"


class GraphPoster:
    def __init__(self):
        from dotenv import load_dotenv

        load_dotenv()
        load_dotenv(Path(__file__).resolve().parent / ".env")
        self.ig_user_id = os.getenv("IG_USER_ID", "me")
        self.token = os.getenv("IG_ACCESS_TOKEN")
        self.base = os.getenv("GRAPH_BASE_URL", DEFAULT_BASE).rstrip("/")
        # Optional: serve images yourself instead of catbox. If set, slide URLs
        # become f"{IMAGE_BASE_URL}/<relative path from repo root>".
        self.image_base_url = os.getenv("IMAGE_BASE_URL", "").rstrip("/")

    # -- image hosting -------------------------------------------------------
    def _host_images(self, images: list[Path]) -> list[str]:
        if self.image_base_url:
            root = Path.cwd()
            urls = []
            for p in images:
                rel = p.resolve().relative_to(root)
                urls.append(f"{self.image_base_url}/{rel}")
            logger.info("Using %d self-hosted image URLs under %s", len(urls), self.image_base_url)
            return urls
        # default: upload each slide to catbox.moe, get a public URL
        urls = []
        for p in images:
            with open(p, "rb") as fh:
                r = requests.post(
                    CATBOX,
                    data={"reqtype": "fileupload"},
                    files={"fileToUpload": (p.name, fh, "image/jpeg")},
                    timeout=120,
                )
            url = r.text.strip()
            if r.status_code != 200 or not url.startswith("http"):
                raise SystemExit(f"Image upload failed for {p.name}: {r.status_code} {url[:200]}")
            logger.info("uploaded %s → %s", p.name, url)
            urls.append(url)
        return urls

    # -- graph helpers -------------------------------------------------------
    def _post(self, path: str, data: dict) -> dict:
        data = {**data, "access_token": self.token}
        r = requests.post(f"{self.base}/{path}", data=data, timeout=120)
        body = r.json()
        if "error" in body:
            raise SystemExit(f"Graph API error ({path}): {body['error'].get('message', body['error'])}")
        return body

    def _get(self, path: str, fields: str) -> dict:
        r = requests.get(f"{self.base}/{path}", params={"fields": fields, "access_token": self.token}, timeout=60)
        body = r.json()
        if "error" in body:
            raise SystemExit(f"Graph API error ({path}): {body['error'].get('message', body['error'])}")
        return body

    def _create_item(self, image_url: str) -> str:
        return self._post(
            f"{self.ig_user_id}/media",
            {"image_url": image_url, "is_carousel_item": "true"},
        )["id"]

    def _create_carousel(self, children: list[str], caption: str) -> str:
        return self._post(
            f"{self.ig_user_id}/media",
            {"media_type": "CAROUSEL", "children": ",".join(children), "caption": caption},
        )["id"]

    def _wait_ready(self, container_id: str, tries: int = 40, delay: float = 3.0) -> None:
        for _ in range(tries):
            status = self._get(container_id, "status_code").get("status_code")
            if status == "FINISHED":
                return
            if status == "ERROR":
                raise SystemExit(f"Container {container_id} failed processing (status ERROR)")
            time.sleep(delay)
        raise SystemExit(f"Container {container_id} not ready after {tries} checks")

    # -- public --------------------------------------------------------------
    def post_carousel(self, images: list[Path], caption: str, **_ignored) -> str:
        if not self.ig_user_id or not self.token:
            raise SystemExit(
                "Missing IG_USER_ID / IG_ACCESS_TOKEN — complete the Graph API "
                "setup in publish/GRAPH_API.md and put them in .env."
            )
        if not 2 <= len(images) <= 10:
            raise SystemExit(f"A carousel needs 2–10 images (got {len(images)})")

        urls = self._host_images(images)
        children = [self._create_item(u) for u in urls]
        logger.info("created %d carousel item containers", len(children))
        carousel = self._create_carousel(children, caption)
        self._wait_ready(carousel)
        media_id = self._post(f"{self.ig_user_id}/media_publish", {"creation_id": carousel})["id"]
        permalink = self._get(media_id, "permalink").get("permalink", "")
        logger.info("published media %s", media_id)
        return permalink or f"(media id {media_id})"
