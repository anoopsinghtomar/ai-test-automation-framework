from models.ollama_client import call_model

def analyze_image(image_description):
    prompt = f"""
    Analyze this UI screenshot description and list:
    - UI bugs
    - UX issues
    - Missing validations

    Description:
    {image_description}
    """
    return call_model("qwen2-vl", prompt)