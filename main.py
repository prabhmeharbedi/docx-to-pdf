from flask import Flask, request, send_file, render_template
import os
from docx2pdf import convert
from PyPDF2 import PdfReader, PdfWriter

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
OUTPUT_FOLDER = './outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def home():
    """
    Render the home page with the upload form.
    """
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle file upload, convert DOCX to PDF, and apply optional password protection.
    """
    # Get the password from the form
    password = request.form.get('password')

    # Check if a file is included in the request
    if 'file' not in request.files:
        return "No file part in the request", 400
    file = request.files['file']

    # Ensure a file is selected
    if file.filename == '':
        return "No file selected", 400

    # Validate file type
    if file and file.filename.endswith('.docx'):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Convert DOCX to PDF
        pdf_path = os.path.join(OUTPUT_FOLDER, file.filename.replace('.docx', '.pdf'))
        convert_to_pdf(filepath, pdf_path)

        # Apply password protection if a password is provided
        if password:
            add_password(pdf_path, password)

        # Send the generated PDF file back to the user
        return send_file(pdf_path, as_attachment=True)

    return "Invalid file type. Please upload a .docx file.", 400


def convert_to_pdf(docx_path, pdf_path):
    """
    Converts a DOCX file to a PDF while preserving the original layout and formatting.
    """
    convert(docx_path, pdf_path)


def add_password(pdf_path, password):
    """
    Adds password protection to a PDF file.
    """
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    # Add all pages from the original PDF to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Encrypt the PDF with the provided password
    writer.encrypt(password)

    # Save the password-protected PDF
    with open(pdf_path, "wb") as protected_pdf:
        writer.write(protected_pdf)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
