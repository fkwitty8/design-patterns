from ...core.interfaces import SupportStrategy
from ...core.models import SupportRequest

class PasswordResetStrategy(SupportStrategy):
    def process(self, request: SupportRequest):
        print(f"SECURITY: Reset link generated for {request.user_email}")