from .versicle import extract_versicles


def process_text(text: str):
    """Process raw text and return structured content."""

    # Detect versicles
    versicles_arr = extract_versicles(text)

    print(versicles_arr)
