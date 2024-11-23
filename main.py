from flask import Flask, request, send_file, render_template
import os
import subprocess

app = Flask(__name__)

# Directories for uploads and outputs
UPLOAD_FOLDER = './uploads'
OUTPUT_FOLDER = './outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

@app.route('/')
def home():
    return render_template('index.html')  # Ensure index.html exists in the templates/ folder

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file and file.filename.endswith('.docx'):
        # Save the uploaded file
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(input_path)

        # Generate the output PDF path
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], file.filename.replace('.docx', '.pdf'))

        # Get optional password from the form
        password = request.form.get('password')

        # Convert DOCX to PDF using unoconv
        try:
            subprocess.run(['unoconv', '-f', 'pdf', '-o', output_path, input_path], check=True)

            # If a password is provided, encrypt the PDF
            if password:
                protected_output_path = os.path.join(app.config['OUTPUT_FOLDER'], f"protected_{file.filename.replace('.docx', '.pdf')}")
                subprocess.run([
                    'qpdf', '--encrypt', password, password, '256',
                    '--', output_path, protected_output_path
                ], check=True)
                output_path = protected_output_path  # Update the path to the encrypted file

        except subprocess.CalledProcessError as e:
            return f"Error during conversion or encryption: {e}", 500

        return send_file(output_path, as_attachment=True)

    else:
        return "Invalid file type. Please upload a .docx file.", 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
