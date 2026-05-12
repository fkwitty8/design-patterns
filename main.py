from src.registry import bootstrap_system
from src.core.models import SupportRequest

def run_demo():
    # Initialize the entire architecture
    platform = bootstrap_system()

    # Create some sample requests
    requests = [
        # SupportRequest("REQ-001", "SECURITY", "PWD_RESET","kiyimba@example.com", {}),
        # SupportRequest("REQ-002", "BILLING", "REFUND","maya@example.com", {"amount": 75.00}),
        # # SupportRequest("REQ-003", "BILLING", "DESPUTE","mushabe@gmail.com", {}),
        SupportRequest("REQ-004", "TECHNICAL", "OUTAG","josh@example.com", {}), # will internally fail and escalate to the fallback chain
        # SupportRequest("REQ-005", "TECHNICAL", "HARDWARE","josh@example.com", {}),
        # SupportRequest("REQ-006", "MANAGEMENT","APPROVAL", "paulline@example.com", {"reason": "Budget override"}),
        # SupportRequest("T4", "GHOST_TYPE","GHOST_TYPE", "hacker@site.com", {}) # Will fall through
    ]

    # Process 
    for req in requests:
        platform.process(req)

if __name__ == "__main__":
    run_demo()