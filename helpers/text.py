def tokenize(text: str) -> list[str]:
    """
    Splits text into tokens by spaces and newlines,
    keeping quotes/numbers attached unless separated by whitespace/newline.
    """
    # Replace newlines with spaces, then split on spaces
    return text.replace("\n", " ").split()
