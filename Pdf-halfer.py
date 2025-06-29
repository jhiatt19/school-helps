from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
import io
import tempfile


def split_pdf_image(pdf_path, output_folder):
    """
    Splits each page of a PDF containing images into two halves (top and bottom).

    Args:
        pdf_path (str): Path to the PDF file.
        output_folder (str): Folder where the split files will be saved.

    Returns:
        None
    """
    try:
        reader = PdfReader(pdf_path)

        for page_num, page in enumerate(reader.pages, start=1):
            # Extract image data from the page
            x_object = page["/Resources"]["/XObject"] if "/XObject" in page["/Resources"] else None

            if x_object:
                for obj in x_object:
                    img = x_object[obj]

                    if img["/Subtype"] == "/Image":
                        size = (img["/Width"], img["/Height"])
                        data = img.get_data()

                        # Create an image from the data
                        with Image.open(io.BytesIO(data)) as pil_img:
                            width, height = pil_img.size

                            # Split the image into top and bottom halves
                            top_half = pil_img.crop((0, 0, width, height // 2))
                            bottom_half = pil_img.crop((0, height // 2, width, height))

                            # Rotate the halves 90 degrees
                            top_half = top_half.rotate(90, expand=True)
                            bottom_half = bottom_half.rotate(90, expand=True)

                            # Save the halves as new PDF pages
                            save_image_as_pdf(top_half, f"{output_folder}/page_{page_num}_top.pdf")
                            save_image_as_pdf(bottom_half, f"{output_folder}/page_{page_num}_bottom.pdf")

            else:
                print(f"No images found on page {page_num}")

    except Exception as e:
        print(f"Error: {e}")


def save_image_as_pdf(image, output_path):
    """
    Saves a PIL Image as a PDF.

    Args:
        image (PIL.Image.Image): The image to save.
        output_path (str): Path to save the PDF.

    Returns:
        None
    """
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
        temp_file_path = temp_file.name
        image.save(temp_file_path, format="JPEG")

        c = canvas.Canvas(output_path, pagesize=letter)
        c.drawImage(temp_file_path, 0, 0, letter[0], letter[1])
        c.save()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Split images in a PDF into top and bottom halves.")
    parser.add_argument("pdf_path", type=str, help="Path to the input PDF file.")
    parser.add_argument("output_folder", type=str, help="Folder to save the split PDF files.")

    args = parser.parse_args()

    split_pdf_image(args.pdf_path, args.output_folder)
