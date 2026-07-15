"""Publish a prepared carousel to Instagram via instagrapi (private API).

Adapted from the asanchezyali/instagram-bot InstagramHumanPoster: it reuses a
saved session to avoid frequent logins and adds small human-like delays.

NOTE: instagrapi drives Instagram's *private* API. It works without a Meta app,
but it is against Instagram's ToS and can trigger temporary blocks. Keep volume
low, keep the session file, and never hard-code credentials (use .env).
"""

from __future__ import annotations

import json
import logging
import os
import random
import time
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("publish.poster")

# Instagram caption hard limit.
MAX_CAPTION = 2200


class InstagramPoster:
    def __init__(self, session_file: str | Path = "publish/.instagram_session.json"):
        from dotenv import load_dotenv  # lazy: only needed to publish

        load_dotenv()
        self.username = os.getenv("INSTAGRAM_USERNAME")
        self.password = os.getenv("INSTAGRAM_PASSWORD")
        self.session_file = Path(session_file)
        self.client = None

    # -- helpers -------------------------------------------------------------
    @staticmethod
    def _delay(lo: float = 1.0, hi: float = 3.0) -> None:
        time.sleep(random.uniform(lo, hi))

    def _save_session(self) -> None:
        if self.client and self.client.get_settings():
            self.session_file.parent.mkdir(parents=True, exist_ok=True)
            self.session_file.write_text(json.dumps(self.client.get_settings()))
            logger.info("Session saved → %s", self.session_file)

    def _load_session(self) -> bool:
        from instagrapi import Client

        if not self.session_file.exists():
            return False
        try:
            self.client = Client()
            self.client.set_settings(json.loads(self.session_file.read_text()))
            self.client.get_timeline_feed()  # validate
            logger.info("Reused saved session")
            return True
        except Exception as e:  # noqa: BLE001
            logger.warning("Saved session invalid (%s); logging in fresh", e)
            return False

    # -- public --------------------------------------------------------------
    def login(self) -> None:
        from instagrapi import Client

        if not self.username or not self.password:
            raise SystemExit(
                "Missing INSTAGRAM_USERNAME / INSTAGRAM_PASSWORD "
                "(set them in a .env file — see publish/.env.example)"
            )
        if self._load_session():
            return
        self.client = Client()
        self._delay(2.0, 4.0)
        self.client.login(self.username, self.password)
        self._save_session()
        logger.info("Logged in as @%s", self.username)

    def post_carousel(self, images: list[Path], caption: str) -> str:
        """Upload an ordered list of JPEGs as one carousel. Returns the post URL."""
        if not images:
            raise SystemExit("No images to publish")
        if len(images) > 10:
            raise SystemExit(f"Instagram carousels allow at most 10 images (got {len(images)})")
        if len(caption) > MAX_CAPTION:
            raise SystemExit(f"Caption is {len(caption)} chars (Instagram max {MAX_CAPTION})")

        self.login()
        self._delay(3.0, 5.0)  # "review" pause before posting
        media = self.client.album_upload(
            paths=[str(p) for p in images],
            caption=caption,
        )
        url = f"https://instagram.com/p/{media.code}"
        logger.info("Posted carousel → %s", url)
        return url
