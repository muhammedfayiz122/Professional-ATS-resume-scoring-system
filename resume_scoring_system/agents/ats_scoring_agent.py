from autogen_agentchat.agents import AssistantAgent

SYSTEM_PROMPT = """
"""
def getATSScoringAgent(model_client):
    """
    Returns ATS Scoring Agent.
    """
    agent = AssistantAgent(
        name="ATS Scoring Agent",
        description="This agent scores resumes based on ATS criteria.",
        system_message=SYSTEM_PROMPT,
        model_client=model_client,
    )