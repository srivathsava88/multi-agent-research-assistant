from agents.gemini_client import model

def planner_agent(topic):

    prompt = f"""
    Create a research plan for:

    {topic}

    Include:
    - Main Topic
    - Subtopics
    - Research Questions
    """

    response = model.generate_content(prompt)

    return response.text