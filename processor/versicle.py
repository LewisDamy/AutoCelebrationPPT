from helpers.json import read_json

OPEN_QUOTE = "\u201C"  # “
CLOSE_QUOTE = "\u201D"  # ”
STRAIGHT_QUOTE = "\""  # "

MATCHES = []


def tokenize(text: str) -> list[str]:
    """
    Splits text into tokens by spaces and newlines,
    keeping quotes/numbers attached unless separated by whitespace/newline.
    """
    # Replace newlines with spaces, then split on spaces
    return text.replace("\n", " ").split()


def is_valid_chapter_versicle(text: str) -> bool:
    parts = text.split(":")
    return len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit()


def contains_open_close_quotes(paragraph: str) -> tuple[str, list[str]]:
    """Check if paragraph contains quotes """
    words = tokenize(paragraph)
    inside_quote = False

    for i, word in enumerate(words):
        # STEP 1 - check if found a OPEN_QUOTE
        if not inside_quote and word.startswith((OPEN_QUOTE, STRAIGHT_QUOTE)):
            inside_quote = True  # Mark that logic is inside quote
            # print(f"Found ENTER quote {word}")

        # STEP 2 - check for the CLOSE_QUOTE
        if inside_quote and word.endswith((CLOSE_QUOTE, STRAIGHT_QUOTE)):
            # print(f"Found CLOSE quote {word}")
            # Collect everything after the ending quote
            return " ".join(words[:i + 1]), words[i + 1:]
    return "", []


def match_bible_book(words: list[str], bible_books_list: list[str]) -> str | None:
    joined_words_with_space = " ".join(words)
    # If exists book GOTTA be the first word or BOOK VERSION of it!
    chapter = words[0].lower() if not words[0].isdigit() else " ".join(words[:2]).lower()

    if chapter in bible_books_list:
        return joined_words_with_space
    return None


def extract_versicles(text):
    counter = 0
    bible_data = read_json("assets/bible/bible_books_list.json")
    bible_books_list = [item["book"].lower() for item in bible_data["books"]]

    # Iterate through the text
    for index, paragraph in enumerate(text.split('\n\n')):
        versicle, after_quote = contains_open_close_quotes(paragraph)
        if len(after_quote) == 0:
            # INVALID QUOTE - continue to iterate in the paragraph
            continue

        valid_reference = match_bible_book(after_quote, bible_books_list)

        if valid_reference:
            MATCHES.append({
                "orderId": index,
                "content": versicle,
                "reference": valid_reference,
                "type": "versicle"
            })
            counter += 1

    print(f"Total versicles found: {counter}")

    return MATCHES
