from ...core.interfaces import BaseHandler
from .strategies import ApprovalStrategy

class ManagementHandler(BaseHandler):
    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        # Vertical Map
        self._strategy_map = {
            "APPROVAL": ApprovalStrategy()
        }