from autogen_agentchat.agents import AssistantAgent

SYSTEM_PROMPT = """
You are an improvement recommendation expert. Your task is to provide recommendations for improving resumes.
"""
def getImprovementRecommendationAgent(model_client):
    """
    Returns Improvement Recommendation Agent.
    """
    agent = AssistantAgent(
        name="Improvement Recommendation Agent",
        description="This agent provides recommendations for improving resumes.",
        system_message=SYSTEM_PROMPT,
        model_client=model_client,
    )
    return agent