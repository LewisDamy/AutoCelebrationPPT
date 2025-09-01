from helpers.text import tokenize

OPEN_QUOTE = "\u201C"  # “
CLOSE_QUOTE = "\u201D"  # ”
STRAIGHT_QUOTE = "\""  # "
DASH_QUOTE = "\u2013"  # -

MATCHES = []


def contains_open_close_quotes(paragraph: str) -> tuple[str, list[str]]:
    """Check if paragraph contains quotes """
    words = tokenize(paragraph)
    inside_quote = False

    for i, word in enumerate(words):
        # STEP 1 - check if found a OPEN_QUOTE
        if not inside_quote and word.startswith((OPEN_QUOTE, STRAIGHT_QUOTE)):
            inside_quote = True  # Mark that logic is inside quote

        # STEP 2 - check for the CLOSE_QUOTE
        if inside_quote and word.endswith((CLOSE_QUOTE, STRAIGHT_QUOTE)):
            # Collect everything after the ending quote
            return " ".join(words[:i + 1]), words[i + 1:]
    return "", []


def contains_dash(arr_words: list[str]) -> tuple[bool, str | None]:
    for i, word in enumerate(arr_words):
        if word == DASH_QUOTE:
            author = " ".join(arr_words[i + 1::])
            return True, author
    return False, None


def extract_quotes(text):
    counter = 0

    # Iterate through the text
    for index, paragraph in enumerate(text.split('\n\n')):
        quote, after_quote = contains_open_close_quotes(paragraph)

        has_dash, reference = contains_dash(after_quote)
        if has_dash:
            MATCHES.append({
                "orderId": index,
                "content": quote,
                "reference": reference,
                "type": "quote"
            })
            counter += 1

    print(f"Total quotes found: {len(MATCHES)}")
    return MATCHES
