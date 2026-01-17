# Re-export from cross_web for backwards compatibility
from cross_web.request._django import AsyncDjangoHTTPRequestAdapter, DjangoHTTPRequestAdapter

__all__ = ["AsyncDjangoHTTPRequestAdapter", "DjangoHTTPRequestAdapter"]
