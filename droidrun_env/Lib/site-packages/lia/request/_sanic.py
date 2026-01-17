# Re-export from cross_web for backwards compatibility
from cross_web.request._sanic import SanicHTTPRequestAdapter, convert_request_to_files_dict

__all__ = ["SanicHTTPRequestAdapter", "convert_request_to_files_dict"]
