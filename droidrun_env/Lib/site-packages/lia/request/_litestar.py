# Re-export from cross_web for backwards compatibility
from cross_web.request._litestar import LitestarRequestAdapter

__all__ = ["LitestarRequestAdapter"]
