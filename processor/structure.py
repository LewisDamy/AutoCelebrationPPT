from .versicle import extract_versicles
from .quotes import extract_quotes
from .all_caps import extract_allcaps


def process_text(text: str):
    """Process raw text and return structured content."""

    # Detect versicles
    versicles_arr = extract_versicles(text)

    quotes_arr = extract_quotes(text)

    allcaps_arr = extract_allcaps(text)

    # print(versicles_arr)
    # print(quotes_arr)
    # print(allcaps_arr)
