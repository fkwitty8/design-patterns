from ...core.interfaces import BaseHandler
from .strategies import OutageStrategy, HardwareStrategy

class TechnicalHandler(BaseHandler):
    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        self._strategy_map = {
            "OUTAGE": OutageStrategy(),
            "HARDWARE": HardwareStrategy()
        }