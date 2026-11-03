import httpx

def read_callback(url: str) -> str:
    return httpx.get(url, timeout=5).text
