from ...core.interfaces import BaseHandler
from .strategies import RefundStrategy,DisputeStrategy

class BillingHandler(BaseHandler):
    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        # Local "Vertical" Map
        self._strategy_map = {
            "REFUND": RefundStrategy(),
            "DESPUTE": DisputeStrategy()
        }