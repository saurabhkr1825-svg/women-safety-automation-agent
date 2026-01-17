# Re-export from cross_web for backwards compatibility
from cross_web.request._quart import QuartHTTPRequestAdapter

__all__ = ["QuartHTTPRequestAdapter"]
