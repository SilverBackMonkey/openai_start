from PyPDF2 import PdfReader
import docx2txt
import csv
import pytesseract
from PIL import Image

# # Open the image file
# image = Image.open('2.png')

# # Use PyTesseract to extract text from the image
# extracted_text = pytesseract.image_to_string(image)

# image.show()
# print(image.format)
# # Print the extracted text
# print(extracted_text)
def extract_text_from_file(file):
    """Return the text content of a file."""
    if file.mimetype == "application/pdf":
        # Extract text from pdf using PyPDF2
        reader = PdfReader(file)
        extracted_text = ""
        for page in reader.pages:
            extracted_text += page.extract_text()
    elif file.mimetype == "text/plain":
        # Read text from plain text file
        extracted_text = file.read().decode("utf-8")
        file.close()
    elif file.mimetype == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        # Extract text from docx using docx2txt
        extracted_text = docx2txt.process(file)
        
    else:
        # Unsupported file type
        raise ValueError("Unsupported file type: {}".format(file.mimetype))

    return extracted_text
