from models.ollama_client import call_model

def generate_test_cases(analysis):
    prompt = f"""
    Based on this UI analysis:

    {analysis}

    Generate:
    1. Test cases
    2. Bug report
    3. Severity levels
    """
    return call_model("llama3", prompt)