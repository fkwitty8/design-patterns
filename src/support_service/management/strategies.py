from ...core.interfaces import SupportStrategy
from ...core.models import SupportRequest

class ApprovalStrategy(SupportStrategy):
    def process(self, request: SupportRequest):
        # Logic to flag this for a manager's dashboard
        reason = request.metadata.get('reason', 'No reason provided')
        print(f"MANAGEMENT: Exceptional approval pending for {request.user_email}. Reason: {reason}")