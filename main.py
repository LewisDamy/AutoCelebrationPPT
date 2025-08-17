import sys
import os
from parsers.docx_parser import parse_docx
from generator.ppt_generator import create_ppt


def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <docx file> <ppt file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Error: {input_file} not found.")
        sys.exit(1)

    # Step 1: Parse input
    docx = parse_docx(input_file)

    # Step 2: Process text (detect structure)
    # TODO

    # Step 3: Generate PowerPoint
    create_ppt(docx, output_file)

    print(f"Presentation created: {output_file}")


if __name__ == "__main__":
    main()
