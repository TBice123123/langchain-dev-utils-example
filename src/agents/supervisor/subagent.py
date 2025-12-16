from langchain.agents import create_agent
from langchain_core.tools import tool

from lib.models import load_chat_model


@tool
def create_calendar_event(
    title: str,
    start_time: str,
    end_time: str,
    attendees: list[str],
    location: str = "",
) -> str:
    """Create a calendar event. Requires precise ISO datetime format."""
    return f"Event created: {title} from {start_time} to {end_time}, with {len(attendees)} attendees"


@tool
def send_email(
    to: list[str],
    subject: str,
    body: str,
    cc: list[str] = [],
) -> str:
    """Send an email using the email API. Requires correct formatted addresses."""
    return f"Email sent to {', '.join(to)} - Subject: {subject}"


@tool
def get_available_time_slots(
    attendees: list[str],
    date: str,
    duration_minutes: int,
) -> list[str]:
    """Query calendar available time slots for participants on a specific date."""
    return ["09:00", "14:00", "16:00"]


model = load_chat_model(
    "openrouter:qwen/qwen-plus",
)


CALENDAR_AGENT_PROMPT = (
    "You are a calendar scheduling assistant. "
    "Parse natural-language scheduling requests (e.g. 'next Tuesday at 2 PM') into correct ISO datetime format. "
    "Use get_available_time_slots to check availability when needed. "
    "Use create_calendar_event to schedule events. "
    "Always confirm what has been scheduled in your final response."
)

calendar_agent = create_agent(
    model,
    tools=[create_calendar_event, get_available_time_slots],
    system_prompt=CALENDAR_AGENT_PROMPT,
    name="calendar_agent",
)

EMAIL_AGENT_PROMPT = (
    "You are an email assistant. "
    "Compose professional emails based on natural-language requests. "
    "Extract recipient information and craft appropriate subject lines and body content. "
    "Use send_email to send the email. "
    "Always confirm in your final response what has been sent."
)

email_agent = create_agent(
    model,
    tools=[send_email],
    system_prompt=EMAIL_AGENT_PROMPT,
    name="email_agent",
)
