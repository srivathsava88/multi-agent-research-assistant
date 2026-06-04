from agents.gemini_client import model

def report_writer(summary):

    prompt = f"""
    Convert this into a professional report.

    {summary}

    Sections:

    1. Executive Summary
    2. Introduction
    3. Findings
    4. Recommendations
    5. Conclusion
    """

    response = model.generate_content(prompt)

    return response.text