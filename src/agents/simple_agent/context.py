from dataclasses import dataclass


@dataclass
class AssistantContext:
    assistant_name: str = "Assistant"
    user_name: str = "Tom"
    user_role: str = "Simple User"
