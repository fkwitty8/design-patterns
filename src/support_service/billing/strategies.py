from ...core.models import SupportRequest
from ...core.interfaces import SupportStrategy

class RefundStrategy(SupportStrategy):
    def process(self, request: SupportRequest):
        amount = request.metadata.get('amount', 0)
        print(f"BILLING: Auto-refunded ${amount} to {request.user_email}")

class DisputeStrategy(SupportStrategy):
    def process(self, request: SupportRequest):
        print(f"BILLING: Dispute case logged. Human intervention required.")