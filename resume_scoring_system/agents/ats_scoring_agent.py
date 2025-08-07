from autogen_agentchat.agents import AssistantAgent

SYSTEM_PROMPT = """
You are an ATS scoring expert. Your task is to score resumes based on ATS criteria.
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
    return agent