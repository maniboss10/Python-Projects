
import os
import requests

BACKEND_API_URL = os.getenv(
    "BACKEND_API_URL",
    "http://127.0.0.1:8000"
)


def check_backend_health():
    try:
        response = requests.get(
            f"{BACKEND_API_URL}/api/health",
            timeout=5
        )

        response.raise_for_status()

        return {
            "success": True,
            "data": response.json()
        }

    except requests.RequestException as error:
        return {
            "success": False,
            "error": str(error)
        }
