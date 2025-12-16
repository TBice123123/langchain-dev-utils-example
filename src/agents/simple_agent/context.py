from dataclasses import dataclass


@dataclass
class AssistantContext:
    assistant_name: str
    user_name: str
    user_role: str
