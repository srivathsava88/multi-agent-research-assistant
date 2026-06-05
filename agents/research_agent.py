from agents.gemini_client import model

def research_agent(section):

    prompt = f"""
    Perform detailed research on:

    {section}

    Include:

    - Explanation
    - Key concepts
    - Examples
    - Recent trends
    - Statistics if available

    Return detailed information.
    """

    response = model.generate_content(prompt)

    return response.text