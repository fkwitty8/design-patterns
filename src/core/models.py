from dataclasses import dataclass

@dataclass
class SupportRequest:
    request_id: str
    request_type: str
    department_type:str
    user_email: str
    metadata: dict