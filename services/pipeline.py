from services.image_analyzer import analyze_image
from services.text_reasoner import generate_test_cases

def run_pipeline(image_description):
    print("🔍 Step 1: Image Analysis...")
    analysis = analyze_image(image_description)

    print("🧠 Step 2: Reasoning...")
    result = generate_test_cases(analysis)

    return result