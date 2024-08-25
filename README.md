# Newsletter Generator in French and Braille

## Description

This project is a deployed Streamlit application that allows users to generate a newsletter from popular articles in French. Users can select a time period, a keyword, and a language (French or Braille) to generate and download the newsletter as a PDF file.

The application uses the NewsAPI to retrieve articles, the Newspaper library to extract the full content of the articles, and a translation function to convert the text into Braille if needed.

## Features

- **Time Period Selection**: Choose to retrieve articles published since yesterday, the last 7 days, or the last 30 days.
- **Keyword**: Filter articles based on specific keywords (technology, culture, France, politics, international).
- **Language**: Select the language for generating the newsletter (French or Braille).
- **Download**: Download the generated newsletter in PDF format.

## Usage

The application is available online via a deployed Streamlit instance. To use it:

1. Access the application via this link:
2. Select the desired time period, keyword, and language.
3. Click "Generate the newsletter."
4. Download the generated PDF file.

## Dependencies

- `streamlit`: To create the user interface.
- `requests`: To interact with the NewsAPI.
- `newspaper`: To extract the content of the articles.
- `fpdf`: To generate PDF files.

## License

This project is licensed under the MIT License. 
