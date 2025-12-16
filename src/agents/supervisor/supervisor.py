from langchain.agents import create_agent
from langchain_dev_utils.agents import wrap_agent_as_tool

from lib.models import load_chat_model
from src.agents.supervisor.subagent import calendar_agent, email_agent


schedule_event = wrap_agent_as_tool(
    calendar_agent,
    "schedule_event",
    tool_description="""Schedule calendar events using natural language.

    Use this when the user wants to create, modify, or check calendar appointments.
    Handles date/time parsing, querying availability, and creating events.

    Input: natural-language calendar scheduling request (e.g. 'meeting with design team next Tuesday at 2 PM')
    """,
)
manage_email = wrap_agent_as_tool(
    email_agent,
    "manage_email",
    tool_description="""Send emails using natural language.

    Use this when the user wants to send notifications, reminders, or any email communication.
    It can extract recipient information, generate subject lines, and compose email content.

    Input: natural-language email request (e.g., 'send them a meeting reminder')f
    """,
)


SUPERVISOR_PROMPT = (
    "You are a helpful personal assistant. "
    "You can schedule calendar events and send emails. "
    "Break down user requests into appropriate tool calls and coordinate the results. "
    "When a request involves multiple actions, use multiple tools in sequence."
)

model = load_chat_model(
    "openrouter:qwen/qwen3-max",
)

supervisor_agent = create_agent(
    model, tools=[schedule_event, manage_email], system_prompt=SUPERVISOR_PROMPT
)
