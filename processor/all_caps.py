BULLET_QUOTE = "\u2022"  # •
ELLIPSES = {"...", "…"}

MATCHES = []


def ends_with_ellipse(text) -> bool:
    return any(text.endswith(e) for e in ELLIPSES)


def extract_allcaps(text):
    counter = 0

    splitted_text = enumerate(text.split('\n\n'))

    # Iterate through the text
    for index, paragraph in splitted_text:
        # Check for All caps and ignore all caps with bullet quote
        if paragraph.isupper() and not paragraph.startswith(BULLET_QUOTE) and not ends_with_ellipse(paragraph):
            MATCHES.append({
                "orderId": index,
                "content": paragraph,
                "type": "all-caps-text"
            })
            counter += 1

    print(f"Total all caps text found: {len(MATCHES)}")
    return MATCHES
