from services.pipeline import run_pipeline

def test_ui_pipeline():
    input_data = "Login screen with missing validation"
    result = run_pipeline(input_data)

    assert "test case" in result.lower()