# Re-export from cross_web for backwards compatibility
from cross_web.request._flask import AsyncFlaskHTTPRequestAdapter, FlaskHTTPRequestAdapter

__all__ = ["AsyncFlaskHTTPRequestAdapter", "FlaskHTTPRequestAdapter"]
