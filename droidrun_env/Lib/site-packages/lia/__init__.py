# This package has been renamed to cross-web.
# This module re-exports all symbols from cross_web for backwards compatibility.

import warnings

warnings.warn(
    "The 'lia' package has been renamed to 'cross_web'. "
    "Please update your imports from 'from lia import ...' to 'from cross_web import ...'. "
    "The 'lia' package will be removed in a future version.",
    DeprecationWarning,
    stacklevel=2,
)

from cross_web import (
    AiohttpHTTPRequestAdapter,
    AsyncDjangoHTTPRequestAdapter,
    AsyncFlaskHTTPRequestAdapter,
    AsyncHTTPRequest,
    AsyncHTTPRequestAdapter,
    BaseRequestProtocol,
    ChaliceHTTPRequestAdapter,
    Cookie,
    DjangoHTTPRequestAdapter,
    FlaskHTTPRequestAdapter,
    FormData,
    HTTPException,
    LitestarRequestAdapter,
    QuartHTTPRequestAdapter,
    Response,
    SanicHTTPRequestAdapter,
    StarletteRequestAdapter,
    SyncHTTPRequestAdapter,
    TestingRequestAdapter,
)

__all__ = [
    "AiohttpHTTPRequestAdapter",
    "AsyncDjangoHTTPRequestAdapter",
    "AsyncFlaskHTTPRequestAdapter",
    "AsyncHTTPRequest",
    "AsyncHTTPRequestAdapter",
    "BaseRequestProtocol",
    "ChaliceHTTPRequestAdapter",
    "Cookie",
    "DjangoHTTPRequestAdapter",
    "FlaskHTTPRequestAdapter",
    "FormData",
    "HTTPException",
    "LitestarRequestAdapter",
    "QuartHTTPRequestAdapter",
    "Response",
    "SanicHTTPRequestAdapter",
    "StarletteRequestAdapter",
    "SyncHTTPRequestAdapter",
    "TestingRequestAdapter",
]
