# Re-export from cross_web for backwards compatibility
from cross_web.request._base import (
    AsyncHTTPRequestAdapter,
    FormData,
    HTTPMethod,
    QueryParams,
    SyncHTTPRequestAdapter,
)

__all__ = [
    "AsyncHTTPRequestAdapter",
    "FormData",
    "HTTPMethod",
    "QueryParams",
    "SyncHTTPRequestAdapter",
]
