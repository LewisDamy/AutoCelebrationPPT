![Python-3.11](https://img.shields.io/badge/python-%3E=3.11-blue?logo=python)

# Auto Celebration PPT

This project automates the process of generating PowerPoint presentations from Word or PDF documents, making it easier
to prepare slides for sermons, preaching, and church celebrations.

## Running the App

You can generate a PowerPoint presentation from a sample Word or PDF file using the `make run` command. All input files
should be placed in the `samples/` folder.

**Usage:**

```bash
make run <input_filename> <output_file>
```

Example:

```bash
make run outline-2025-08-17.docx slides-2025-08-17.pptx
```

Notes:

- Only .docx file are supported as input (yet).
- Make sure dependencies are installed using:

```bash
make install
```
