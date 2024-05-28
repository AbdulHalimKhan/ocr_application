from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
from docx import Document
import re
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if necessary

def clean_text(text):
    cleaned_text = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', text)
    return cleaned_text

def pdf_to_text(pdf_path):
    document = fitz.open(pdf_path)
    full_text = ""

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text = page.get_text()
        if text:
            full_text += text
        else:
            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = document.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                image = Image.open(io.BytesIO(image_bytes))
                page_text = pytesseract.image_to_string(image)
                full_text += page_text + "\n"

    cleaned_text = clean_text(full_text)
    return cleaned_text

def image_to_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    cleaned_text = clean_text(text)
    return cleaned_text

def save_text_to_doc(text, doc_path):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(doc_path)

def save_text_to_txt(text, txt_path):
    with open(txt_path, 'w') as file:
        file.write(text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        if filename.lower().endswith('.pdf'):
            extracted_text = pdf_to_text(file_path)
        else:
            extracted_text = image_to_text(file_path)

        txt_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.txt')
        doc_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.docx')
        save_text_to_txt(extracted_text, txt_path)
        save_text_to_doc(extracted_text, doc_path)

        return render_template('result.html', txt_path=txt_path, doc_path=doc_path, ocr_text=extracted_text)

@app.route('/download/<file_type>')
def download_file(file_type):
    if file_type == 'txt':
        path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.txt')
    elif file_type == 'docx':
        path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.docx')
    else:
        return 'Invalid file type'
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
