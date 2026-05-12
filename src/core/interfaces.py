from abc import ABC, abstractmethod
from typing import Optional, Dict
from .models import SupportRequest

class SupportStrategy(ABC):
    @abstractmethod
    def process(self, request: SupportRequest) -> None: pass

class BaseHandler(ABC):
    def __init__(self, next_handler: Optional['BaseHandler'] = None):
        self._next = next_handler
        self._strategy_map: Dict[str, SupportStrategy] = {}

    def handle(self, request: SupportRequest, is_fallback: bool = False) -> bool:
        strategy = self._strategy_map.get(request.department_type)

        # local "Vertical" Routing (Strategy Map)
        if strategy:
            strategy.process(request)
            return True
        
        # Horizontal Fallback
        if self._next:
            print(f"[{self.__class__.__name__}] Wrong module. Trying next...")
            return self._next.handle(request, is_fallback=True)
            
        return False