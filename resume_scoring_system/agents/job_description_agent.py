from autogen_agentchat.agents import AssistantAgent

SYSTEM_PROMPT = """
"""
def getJobDescriptionAgent(model_client):
    """
    Returns Job Description Agent.
    """
    agent = AssistantAgent(
        name="Job Description Agent",
        description="This agent processes job descriptions and extracts relevant information.",
        system_message=SYSTEM_PROMPT,
        model_client=model_client,
    )