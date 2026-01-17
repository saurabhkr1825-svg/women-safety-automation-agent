# Re-export from cross_web for backwards compatibility
from cross_web.request._chalice import ChaliceHTTPRequestAdapter

__all__ = ["ChaliceHTTPRequestAdapter"]
