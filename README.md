

# Python Utility Apps

This repository contains five utility apps built in Python that allow users to perform various operations on different types of files, including Word documents, Excel spreadsheets, PDFs, and audio files. Each app is designed with a modern and user-friendly GUI using Tkinter and `ttkbootstrap`.

## 1. **Word Utility App**
A Python application for managing Word documents. It allows users to extract text from Word files, merge multiple Word files, convert Word documents to PDF, set document passwords, and search for specific text within a document.

### Features:
- Extract text from Word documents.
- Merge multiple Word files.
- Convert Word documents to PDF.
- Set a password for Word documents.
- Search for specific text in a Word document.

### Requirements:
- `python-docx` (for Word file manipulation)
- `comtypes` (for COM interaction with MS Word)
- `fpdf` (for PDF conversion)
- `tkinter` (for GUI)

### How to Use:
1. Open the app.
2. Select the desired functionality (e.g., "Extract Text" or "Merge Files").
3. Follow the on-screen prompts to load the Word document and perform the selected action.

---

## 2. **Excel Utility App**
This app is designed to simplify the handling of Excel files. It provides features for filtering, sorting, creating pivot tables, converting to CSV, and generating data visualizations.

### Features:
- Convert Excel files to CSV.
- Filter and sort data based on user inputs.
- Create pivot tables from data.
- Generate various types of charts and visualizations (line, bar, scatter, histogram, box plots).
- Convert Excel data to Word format.

### Requirements:
- `pandas` (for data manipulation)
- `openpyxl` (for Excel file manipulation)
- `matplotlib` (for data visualization)
- `seaborn` (for advanced visualizations)
- `fpdf` (for Word and PDF operations)
- `ttkbootstrap` (for GUI styling)

### How to Use:
1. Open the app.
2. Browse for an Excel file to load.
3. Use the available tabs to perform different operations like filtering, creating pivot tables, or generating charts.
4. Save the output in your preferred format (e.g., CSV, Word, or Excel).

---

## 3. **PDF Utility App**
This app allows users to manage and modify PDF files. It includes features to merge, split, rotate, and extract text from PDFs.

### Features:
- Merge multiple PDF files into one.
- Split PDF files by page ranges.
- Rotate PDF pages.
- Extract text from PDF documents.

### Requirements:
- `PyPDF2` (for PDF manipulation)
- `tkinter` (for GUI)

### How to Use:
1. Open the app.
2. Choose the desired functionality (e.g., "Merge PDFs" or "Extract Text").
3. Follow the prompts to select the PDF files and perform the action.

---

## 4. **Audio Recording App**
This app provides a simple interface for recording, playing, and managing audio files. It includes options for saving, deleting, and renaming audio files.

### Features:
- Record audio from a microphone.
- Play back recorded audio.
- Save recorded audio files in WAV format.
- Delete and rename audio files.

### Requirements:
- `sounddevice` (for audio recording)
- `pydub` (for audio manipulation)
- `tkinter` (for GUI)

### How to Use:
1. Open the app.
2. Click "Record" to start capturing audio.
3. Once recorded, you can save the file, play it back, or delete it.
4. Use the file management options to rename or delete files.

---

## 5. **Enhanced Excel Utility App**
A more advanced version of the Excel utility app, featuring additional functionality like advanced sorting, pivot tables, data visualization, and Excel-to-Word conversion.

### Features:
- Convert Excel to CSV.
- Filter and sort Excel data.
- Create pivot tables.
- Generate various types of charts.
- Convert Excel data to Word documents.

### Requirements:
- `pandas`
- `openpyxl`
- `matplotlib`
- `seaborn`
- `fpdf`
- `docx`
- `ttkbootstrap`

### How to Use:
1. Open the app and browse for an Excel file.
2. Navigate through the available tabs for various tasks, such as filtering data, creating pivot tables, or visualizing the data.
3. Perform the desired actions and save the output files as needed.

---

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/python-utility-apps.git
   ```

2. Install required dependencies for each app. You can use `pip` to install the necessary libraries:

   ```bash
   pip install pandas openpyxl matplotlib seaborn fpdf python-docx PyPDF2 sounddevice pydub ttkbootstrap
   ```

3. Run the app:
   - Navigate to the directory where the app is located.
   - Run the corresponding Python script (e.g., `python word.py`, `python excel.py`).


