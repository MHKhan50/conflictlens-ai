import os
import requests
from dotenv import load_dotenv

load_dotenv()

class OllamaError(RuntimeError):
    pass

def chat(model: str, system: str, user: str) -> str:
    base = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").rstrip("/")
    timeout = int(os.getenv("REQUEST_TIMEOUT", "240"))
    payload = {
        "model": model,
        "stream": False,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "options": {"temperature": 0.2},
    }
    try:
        response = requests.post(f"{base}/api/chat", json=payload, timeout=timeout)
        response.raise_for_status()
        data = response.json()
        return data["message"]["content"].strip()
    except requests.RequestException as exc:
        raise OllamaError(
            f"Could not reach Ollama at {base}. Is Ollama running? Details: {exc}"
        ) from exc
    except (KeyError, ValueError) as exc:
        raise OllamaError(f"Unexpected response from Ollama: {exc}") from exc
