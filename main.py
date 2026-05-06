from services.pipeline import run_pipeline

if __name__ == "__main__":
    image_description = """
    Login page with:
    - Username field
    - Password field
    - Login button
    Error message overlaps UI
    No validation for empty fields
    """

    output = run_pipeline(image_description)
    print("\n=== FINAL OUTPUT ===\n")
    print(output)