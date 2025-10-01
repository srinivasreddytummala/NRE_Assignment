import requests
from typing import List, Dict


def fetch_devices(api_url: str, timeout: int = 5) -> List[Dict]:
    """
    Fetch the device list from API. Returns [] on error.
    """
    try:
        resp = requests.get(api_url, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, list):
            return data
        return []
    except requests.RequestException:
        return []
