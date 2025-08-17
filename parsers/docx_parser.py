import docx

def parse_docx(filename):
    try:
        #Load the document
        doc = docx.Document(filename)
 
        #Extract text from the document
        full_text=[]
        for paragraph in doc.paragraphs:
            full_text.append(paragraph.text)
           
        return "\n\n".join(full_text)
    except FileNotFoundError:
        print(f"Error parsing {filename}: File not found.")
        return None
    except Exception as e:
        print(f"Error parsing {filename}: {e}")
        return None
