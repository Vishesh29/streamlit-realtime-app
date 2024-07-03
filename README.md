# streamlit-realtime-app
This repository contains a Python application designed for real-time data processing and analysis using Streamlit. The application leverages Python's capabilities to handle data streams efficiently, making it suitable for real-time monitoring, analytics, or other dynamic data-driven tasks.

Features
The Python applications in the repository include:

- Language Translation: Translates text from one language to another.
- Email Processing: Sends emails to recipients.
- Password Checker: Evaluates the uniqueness of passwords.
- PDF Operations: Merges, rotates, or adds watermarks to PDF files.
- Image Processing: Performs tasks such as blurring, smoothing, rotating, cropping, creating thumbnails, converting to grayscale, Perspective Transform and resizing images.

## Installation
To run this application, you'll need to have Python installed on your machine. We recommend using a virtual environment to manage your dependencies.

### 1. Clone the repository:
```
git clone https://github.com/Vishesh29/streamlit-realtime-app.git
cd streamlit-realtime-app
```
### 2: Create a virtual environment (Optional but recommended):
```
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```
### 3. Install the required packages:
```
pip install -r requirements.txt
```

### 4. Usage Documentation:

#### 1.  File and Text Translator
This Streamlit app allows users to translate text and text files between multiple languages. Users can choose between translating a block of text or uploading a text file for translation. The app supports several common languages and includes options for auto-detecting the source language.

#### Features
- Text Translation: Enter text directly into the app and translate it to the desired language.
- File Translation: Upload a .txt file and translate its contents.
- Language Support: Supports translation between multiple languages, including but not limited to English, Japanese, Spanish, French, German, Chinese, Russian, Korean, Portuguese, Italian, Arabic, Hindi, Bengali, Urdu, and Punjabi.
- Auto-Detection: Option to auto-detect the source language.
- Download Translated File: After translating a file, download the translated content as a new text file.


#### How to use:
```
streamlit run langauge_translator/streamlit_app.py
```

- Navigate to the App in Your Browser: Open the URL provided by Streamlit (typically http://localhost:8501).
