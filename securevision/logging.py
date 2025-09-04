import logging, sys
from contextvars import ContextVar

request_id_var: ContextVar[str] = ContextVar("request_id", default="-")

class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id_var.get("-")
        return True

def setup_logging(level="INFO"):
    handler = logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter(fmt="level=%(levelname)s msg=%(message)s request_id=%(request_id)s")
    handler.setFormatter(fmt)
    root = logging.getLogger()
    root.setLevel(level)
    root.handlers = [handler]
    root.addFilter(RequestIdFilter())
    return root
