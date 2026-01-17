# Re-export from cross_web for backwards compatibility
from cross_web.request._aiohttp import AiohttpHTTPRequestAdapter

__all__ = ["AiohttpHTTPRequestAdapter"]
