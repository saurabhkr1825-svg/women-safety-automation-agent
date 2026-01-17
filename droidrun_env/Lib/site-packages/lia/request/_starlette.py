# Re-export from cross_web for backwards compatibility
from cross_web.request._starlette import StarletteRequestAdapter

__all__ = ["StarletteRequestAdapter"]
