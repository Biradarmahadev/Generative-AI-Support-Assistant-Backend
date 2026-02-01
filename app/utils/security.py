import time
from fastapi import HTTPException

REQUEST_LIMIT = 5      # requests
TIME_WINDOW = 60       # seconds

_client_requests = {}

def rate_limiter(client_id: str):
    now = time.time()
    window_start = now - TIME_WINDOW

    requests = _client_requests.get(client_id, [])
    requests = [t for t in requests if t > window_start]

    if len(requests) >= REQUEST_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Please try again later."
        )

    requests.append(now)
    _client_requests[client_id] = requests
