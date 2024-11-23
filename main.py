import os
from flask import Flask, request, jsonify, send_file, render_template
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
OUTPUT_FOLDER = './outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def convert_docx_to_pdf(docx_path, pdf_path):
    """Converts a DOCX file to PDF."""
    document = Document(docx_path)
    pdf = canvas.Canvas(pdf_path, pagesize=letter)

    # Add content from DOCX to the PDF
    width, height = letter
    y = height - 50  # Start position for writing text
    for paragraph in document.paragraphs:
        if y <= 50:  # Move to a new page if content exceeds
            pdf.showPage()
            y = height - 50
        pdf.drawString(50, y, paragraph.text)
        y -= 20  # Move down for the next line

    pdf.save()

def add_password_to_pdf(input_pdf_path, output_pdf_path, password):
    """Adds a password to the PDF."""
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    # Add password to the PDF
    writer.encrypt(user_password=password, owner_password=password)

    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    password = request.form.get('password')  # Optional password
    if file.filename == '':
        return "No selected file", 400
    if file and file.filename.endswith('.docx'):
        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(OUTPUT_FOLDER, file.filename.replace('.docx', '.pdf'))
        protected_output_path = os.path.join(OUTPUT_FOLDER, file.filename.replace('.docx', '_protected.pdf'))

        # Save the uploaded file
        file.save(input_path)

        # Convert DOCX to PDF
        try:
            convert_docx_to_pdf(input_path, output_path)
            if password:
                add_password_to_pdf(output_path, protected_output_path, password)
                return send_file(protected_output_path, as_attachment=True)
            else:
                return send_file(output_path, as_attachment=True)
        except Exception as e:
            return f"Error during conversion: {e}", 500

    else:
        return "Invalid file type. Please upload a .docx file.", 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
