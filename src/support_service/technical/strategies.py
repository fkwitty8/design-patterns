from ...core.interfaces import SupportStrategy
from ...core.models import SupportRequest

class OutageStrategy(SupportStrategy):
    def process(self, request: SupportRequest):
        # Logic to notify the On-Call rotation (PagerDuty, etc.)
        print(f"TECH: ALERT! Service outage reported. Notifying engineering team.")

class HardwareStrategy(SupportStrategy):
    def process(self, request: SupportRequest):
        print(f"TECH: Hardware diagnostic initiated for ticket {request.request_id}.")