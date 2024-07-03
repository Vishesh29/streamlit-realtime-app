# streamlit-realtime-app

## Documentation for File and Text Translator
This Streamlit app allows users to translate text and text files between multiple languages. Users can choose between translating a block of text or uploading a text file for translation. The app supports several common languages and includes options for auto-detecting the source language.

### Features
- Text Translation: Enter text directly into the app and translate it to the desired language.
- File Translation: Upload a .txt file and translate its contents.
- Language Support: Supports translation between multiple languages, including but not limited to English, Japanese, Spanish, French, German, Chinese, Russian, Korean, Portuguese, Italian, Arabic, Hindi, Bengali, Urdu, and Punjabi.
- Auto-Detection: Option to auto-detect the source language.
- Download Translated File: After translating a file, download the translated content as a new text file.


### How to use:
```
streamlit run streamlit_app.py
```

- Navigate to the App in Your Browser: Open the URL provided by Streamlit (typically http://localhost:8501).

### Usage
- Select Translation Type:

  - Choose "Translate Text" to translate a block of text.
  - Choose "Translate File" to upload and translate a text file.

- Select Source and Target Languages:

  - Use the dropdown menus to select the source and target languages. The source language can be set to "Auto-detect".

- Enter Text or Upload File:

  - For text translation, enter the text in the provided text area and click "Translate".
  - For file translation, upload a .txt file and click "Translate".

- View Translated Text:

  - For text translation, the translated text will be displayed below the input area.
  - For file translation, the translated text will be displayed, and a download button will be provided to download the translated content.

### Example
- Text Translation
  - Select "Translate Text".
  - Choose "English" as the source language and "Japanese" as the target language.
  - Enter the text "Hello, how are you?" and click "Translate".
  - The translated text "こんにちは、お元気ですか？" will be displayed.

- File Translation
  - Select "Translate File".
  - Choose "Auto-detect" as the source language and "Spanish" as the target language.
  - Upload a text file containing the text "Good morning, have a nice day!".
  - Click "Translate".
  - The translated text "Buenos días, ¡que tengas un buen día!" will be displayed, and a button will allow you to download the translated file.
