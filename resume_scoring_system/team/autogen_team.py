from autogen_agentchat.teams import RoundRobinGroupChat
from resume_scoring_system.agents.resume_processing_agent import getResumeProcessingAgent
from resume_scoring_system.agents.ats_scoring_agent import getATSScoringAgent   
from resume_scoring_system.agents.improvement_recommendation_agent import getImprovementRecommendationAgent
from resume_scoring_system.agents.visualization_agent import getVisualizationAgent
from resume_scoring_system.agents.job_description_agent import getJobDescriptionAgent 
from autogen_agentchat.conditions import TextMentionTermination, TokenUsageTermination

MAX_TOKEN = 5000  # Define a maximum token limit for termination

def getAutogenTeam(model_client):
    """
    Returns the Autogen Team for resume scoring system.
    """
    # Create agents
    resume_processing_agent = getResumeProcessingAgent(model_client)
    ats_scoring_agent = getATSScoringAgent(model_client)
    job_description_agent = getJobDescriptionAgent(model_client)
    improvement_agent = getImprovementRecommendationAgent(model_client)
    visualization_agent = getVisualizationAgent(model_client)
    
    # Define termination condition
    termination = TextMentionTermination("TERMINATE") | TokenUsageTermination(MAX_TOKEN)

    # Create the team with agents
    team = RoundRobinGroupChat(
        participants=[
            resume_processing_agent,
            ats_scoring_agent,
            job_description_agent,
            improvement_agent,
            visualization_agent,
        ],
        max_turns=5,
        termination_condition=termination
    )
    return team