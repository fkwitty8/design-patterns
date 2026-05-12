from ...core.interfaces import BaseHandler
from .strategies import PasswordResetStrategy

class SecurityHandler(BaseHandler):
    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        self._strategy_map = {
            "PWD_RESET": PasswordResetStrategy()
        }