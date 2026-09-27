"""
Gemini provider implementation (added: Google Gemini support).
"""

import os
from typing import Tuple, Optional

from .base import BaseProvider


class GeminiProvider(BaseProvider):
    """
    Provider implementation for Google's Gemini API.
    """

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Gemini API key not found. Set the GOOGLE_API_KEY environment variable."
            )
        self.model = model or os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        # sanitize proxy env: IPv6 no_proxy entries crash httpx used by the SDK
        for var in ("no_proxy", "NO_PROXY"):
            if os.environ.get(var, "").startswith("[") or "[" in os.environ.get(var, ""):
                os.environ[var] = "localhost,127.0.0.1"

        from google import genai
        self.client = genai.Client(api_key=self.api_key)

    def send_prompt(self, prompt: str) -> Tuple[str, int]:
        resp = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )
        text = resp.text or ""
        # rough token estimate when usage metadata is unavailable
        tokens = 0
        try:
            usage = getattr(resp, "usage_metadata", None)
            if usage is not None:
                tokens = (usage.prompt_token_count or 0) + (usage.candidates_token_count or 0)
        except Exception:
            pass
        if not tokens:
            tokens = max(1, len(text.split()))
        return text, tokens

    @property
    def name(self) -> str:
        return "gemini"

    @property
    def supports_streaming(self) -> bool:
        return False
