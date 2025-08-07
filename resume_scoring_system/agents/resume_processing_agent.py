from autogen_agentchat.agents import AssistantAgent

SYSTEM_PROMPT = """
You are a resume processing expert. Your task is to process resumes and extract relevant information.
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
    return agent