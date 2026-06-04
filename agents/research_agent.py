from agents.gemini_client import model

def research_agent(plan):

    prompt = f"""
    Perform detailed research.

    Research Plan:

    {plan}

    Include:
    - Key Findings
    - Trends
    - Examples
    """

    response = model.generate_content(prompt)

    return response.text