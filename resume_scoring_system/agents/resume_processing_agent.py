from autogen_agentchat.agents import AssistantAgent

SYSTEM_PROMPT = """
"""
def getResumeProcessingAgent(model_client):
    """
    Returns Resume Processing Agent.
    """
    agent = AssistantAgent(
        name="Resume Processing Agent",
        description="This agent processes resumes and extracts relevant information.",
        system_message=SYSTEM_PROMPT,
        model_client=model_client,
    )