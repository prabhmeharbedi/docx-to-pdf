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
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    password = request.form.get('password')
    if 'file' not in request.files:
        return "No file part in the request", 400
    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400
    if file and file.filename.endswith('.docx'):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        pdf_path = os.path.join(OUTPUT_FOLDER, file.filename.replace('.docx', '.pdf'))
        convert_to_pdf(filepath, pdf_path)
        if password:
            add_password(pdf_path, password)
        return send_file(pdf_path, as_attachment=True)
    return "Invalid file type. Please upload a .docx file.", 400


def convert_to_pdf(docx_path, pdf_path):
    convert(docx_path, pdf_path)


def add_password(pdf_path, password):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(password)
    with open(pdf_path, "wb") as protected_pdf:
        writer.write(protected_pdf)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Dynamically get the port
    app.run(debug=False, host="0.0.0.0", port=port)
