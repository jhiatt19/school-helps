from pytesseract import image_to_string
from pdf2image import convert_from_path

def ocr_extract_text_from_pdf(pdf_path):
    # Convert PDF pages to images
    images = convert_from_path(pdf_path)
    text = ""

    for page_number, image in enumerate(images, start=1):
        # Perform OCR on each page
        page_text = image_to_string(image)
        text += f"--- Page {page_number} ---\n{page_text}\n"

    return text

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract text from a PDF using OCR.")
    parser.add_argument("pdf_path", type=str, help="Path to the PDF file.")
    parser.add_argument("output_file", type=str, help="Path to save the extracted text.")

    args = parser.parse_args()

    extracted_text = ocr_extract_text_from_pdf(args.pdf_path)

    # Save the extracted text to a file
    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(extracted_text)

    print(f"Extracted text saved to {args.output_file}")

