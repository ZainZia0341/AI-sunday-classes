"""Small helpers shared by all notebooks (Gemini calls + data loading)."""
import json
import os
import time
from pathlib import Path

import numpy as np
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
EMBED_MODEL = os.getenv("GEMINI_EMBED_MODEL", "gemini-embedding-001")

_client = None


def client():
    """Create the Gemini client once and reuse it."""
    global _client
    if _client is None:
        key = os.getenv("GEMINI_API_KEY")
        if not key:
            raise RuntimeError("GEMINI_API_KEY is missing. Copy .env.example to .env and paste your key.")
        _client = genai.Client(api_key=key)
    return _client


def load_data():
    """Load every prompt / sample dataset used in the notebooks."""
    path = Path(__file__).parent / "data" / "eval_data.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _generate(contents, system=None, temperature=0.0, as_json=False, model=None, retries=5):
    config = types.GenerateContentConfig(
        system_instruction=system,
        temperature=temperature,
        response_mime_type="application/json" if as_json else None,
    )
    for attempt in range(retries):
        try:
            resp = client().models.generate_content(model=model or MODEL, contents=contents, config=config)
            return json.loads(resp.text) if as_json else resp.text
        except Exception as e:  # rate limits (free tier) or temporary errors
            if attempt == retries - 1:
                raise
            wait = 10 * (attempt + 1)
            print(f"[retry {attempt + 1}] {type(e).__name__}: waiting {wait}s")
            time.sleep(wait)


def ask(prompt, system=None, temperature=0.0, as_json=False, model=None):
    """One prompt in, one answer out. as_json=True returns a Python dict."""
    return _generate(prompt, system, temperature, as_json, model)


def chat(history, system=None, temperature=0.0, model=None):
    """history = [{"role": "user" | "assistant", "content": "..."}, ...]"""
    contents = [
        types.Content(role="model" if m["role"] == "assistant" else "user",
                      parts=[types.Part(text=m["content"])])
        for m in history
    ]
    return _generate(contents, system, temperature, False, model)


def embed(texts):
    """Turn a list of texts into a numpy matrix (one row per text)."""
    r = client().models.embed_content(model=EMBED_MODEL, contents=texts)
    return np.array([e.values for e in r.embeddings])


def cosine(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
