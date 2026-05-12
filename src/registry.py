from src.support_service.security.handler import SecurityHandler
from src.support_service.billing.handler import BillingHandler
from src.support_service.technical.handler import TechnicalHandler
from src.support_service.management.handler import ManagementHandler
from .platform import SupportPlatform

def bootstrap_system() -> SupportPlatform:
    """
    The ONLY place where modules meet.
    We inject the 'Internal API' chain here.
    """
    # Establish the Chain (Vertical Escalation)
    # Management is the terminal node (None)
    management = ManagementHandler(next_handler=None)
    tech = TechnicalHandler(next_handler=management)
    billing = BillingHandler(next_handler=tech)
    security = SecurityHandler(next_handler=billing)

    # Establish the Horizontal Router (The Speed Path startegy Map)
    route_map = {
        "SECURITY": security,
        "BILLING": billing,
        "TECHNICAL": tech,
        "MANAGEMENT": management
    }

    # Return the fully wired platform
    # Fallback_chain starts at security and walks all the way to management
    return SupportPlatform(routing_map=route_map, fallback_chain=security)