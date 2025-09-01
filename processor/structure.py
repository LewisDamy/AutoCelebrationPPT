from .versicle import extract_versicles
from .quotes import extract_quotes


def process_text(text: str):
    """Process raw text and return structured content."""

    # Detect versicles
    versicles_arr = extract_versicles(text)

    quotes_arr = extract_quotes(text)

    # print(versicles_arr)
    # print(quotes_arr)
