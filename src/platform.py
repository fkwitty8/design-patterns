from typing import Dict
from src.core.interfaces import BaseHandler
from src.core.models import SupportRequest

class SupportPlatform:
    def __init__(self, routing_map: Dict[str, BaseHandler], fallback_chain: BaseHandler):
        self._routing_map = routing_map
        self._fallback_chain = fallback_chain

    def process(self, request: SupportRequest):
        print(f"\n--- Processing {request.request_id} ---")
        # Direct Horizontal Routing 
        handler = self._routing_map.get(request.request_type)
        
        handled = False
        if handler:
            handled = handler.handle(request)
        if not handled:
            print(f"Router: Direct route failed for {request.request_type}. Starting FULL chain search...")
            success = self._fallback_chain.handle(request)
            
            if not success:
                print(f"CRITICAL: No module in the entire company handles {request.request_type} -> {request.department_type}")
                print(f"Issue sent logged and sent to manager deck")