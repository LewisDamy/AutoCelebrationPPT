import json
from pathlib import Path


def read_json(file_path: str):
    """
    Read a JSON file and return its contents as a Python object.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict | list: Parsed JSON content.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"JSON file not found: {file_path}")

    with path.open("r", encoding="utf-8") as f:
        return json.load(f)
