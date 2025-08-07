from autogen_agentchat.agents import AssistantAgent

SYSTEM_PROMPT = """
You are a data visualization expert. Your task is to create visual representations of resume data.
"""
def getVisualizationAgent(model_client):
    """
    Returns Visualization Agent.
    """
    agent = AssistantAgent(
        name="Visualization Agent",
        description="This agent creates visual representations of resume data.",
        system_message=SYSTEM_PROMPT,
        model_client=model_client,
    )
    return agent