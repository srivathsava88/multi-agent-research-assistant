from agents.gemini_client import model

def summarizer(data):

    prompt = f"""
    Summarize this research.

    {data}

    Provide:
    - Key Insights
    - Opportunities
    - Risks
    """

    response = model.generate_content(prompt)

    return response.text