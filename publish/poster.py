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

        # Accept credentials from either the repo-root .env or publish/.env.
        load_dotenv()  # cwd/.env (and upward)
        load_dotenv(Path(__file__).resolve().parent / ".env")  # publish/.env
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

    def _new_client(self):
        """Plain client, matching the setup the account last logged in with
        (asanchezyali/instagram-bot on instagrapi 2.1.2). We deliberately do
        NOT seed a locale/device: the pinned instagrapi version already carries
        the device/app-version fingerprint Instagram associates with this
        account, and overriding the region only looks more suspicious."""
        from instagrapi import Client

        client = Client()
        client.delay_range = [1, 3]  # human-ish pacing between API calls
        client.challenge_code_handler = self._challenge_code_handler
        return client

    @staticmethod
    def _challenge_code_handler(username: str, choice) -> str:
        """Instagram issued an email/SMS checkpoint — ask for the code.

        Needs an interactive terminal (run via `!` in the prompt). In a
        non-interactive run there is no stdin, so we fail with clear guidance
        instead of hanging.
        """
        source = getattr(choice, "name", str(choice))
        print(f"\n🔐 Instagram sent a verification code via {source} for @{username}.")
        try:
            return input("   Enter the code: ").strip()
        except EOFError as exc:
            raise SystemExit(
                "Instagram needs an email/SMS verification code, which requires an "
                "interactive terminal. Re-run the publish command yourself with the "
                "`!` prefix so you can type the code when prompted."
            ) from exc

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
    def login(self, verification_code: str = "") -> None:
        if not self.username or not self.password:
            raise SystemExit(
                "Missing INSTAGRAM_USERNAME / INSTAGRAM_PASSWORD "
                "(set them in a .env file — see publish/.env.example)"
            )
        if self._load_session():
            return
        self.client = self._new_client()
        self._delay(2.0, 4.0)
        # verification_code is the 2FA (authenticator/SMS) code, if 2FA is on.
        self.client.login(self.username, self.password, verification_code=verification_code)
        self._save_session()
        logger.info("Logged in as @%s", self.username)

    def post_carousel(self, images: list[Path], caption: str, verification_code: str = "") -> str:
        """Upload an ordered list of JPEGs as one carousel. Returns the post URL."""
        if not images:
            raise SystemExit("No images to publish")
        if len(images) > 10:
            raise SystemExit(f"Instagram carousels allow at most 10 images (got {len(images)})")
        if len(caption) > MAX_CAPTION:
            raise SystemExit(f"Caption is {len(caption)} chars (Instagram max {MAX_CAPTION})")

        self.login(verification_code=verification_code)
        self._delay(3.0, 5.0)  # "review" pause before posting
        media = self.client.album_upload(
            paths=[str(p) for p in images],
            caption=caption,
        )
        url = f"https://instagram.com/p/{media.code}"
        logger.info("Posted carousel → %s", url)
        return url
