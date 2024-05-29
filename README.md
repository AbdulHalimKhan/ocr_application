# OCR Application

## Overview

This OCR (Optical Character Recognition) Application is a web-based tool that allows users to upload PDF or image files and extract text from them using OCR technology. The extracted text can be previewed and downloaded in either TXT or DOCX format. The application is built with Python, Flask, and Tesseract OCR, and features an attractive and user-friendly interface.

## Features

- **Upload Files**: Users can upload PDF or image files (JPG, PNG, etc.).
- **OCR Processing**: The application processes the uploaded files to extract text using Tesseract OCR.
- **Text Preview**: Users can preview the extracted text on the web page.
- **Download Options**: Users can download the extracted text as a TXT file or a DOCX document.
- **Responsive Design**: The application features a modern and responsive design using Bootstrap and custom CSS.


## Installation

### Prerequisites

- Python 3.6+
- Tesseract OCR

### Steps

1. **Clone the repository:**

    ```sh
    git clone https://github.com/AbdulHalimKhan/ocr_application.git
    cd ocr_application
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Install Tesseract OCR:**

    Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).

    Make sure to add Tesseract to your system's PATH. For example, on Windows, the path might be `C:\Program Files\Tesseract-OCR\tesseract.exe`.

5. **Run the application:**

    ```sh
    python app.py
    ```

6. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

1. **Upload a File:**

    On the homepage, click on the "Choose file" button and select a PDF or image file from your device. Then, click the "Upload" button.

2. **Preview Extracted Text:**

    After the file is uploaded and processed, you will see a preview of the extracted text.

3. **Download Extracted Text:**

    You can choose to download the extracted text as a TXT file or a DOCX document by clicking the respective buttons.

