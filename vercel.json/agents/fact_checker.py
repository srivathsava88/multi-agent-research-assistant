from agents.gemini_client import model

def fact_checker(research):

    prompt = f"""
    Review the following research.

    {research}

    Check:
    - Consistency
    - Weak Claims
    - Missing Evidence
    """

    response = model.generate_content(prompt)

    return response.text