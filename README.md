# PDF Text Selector & Annotation Tool

A professional, lightweight desktop application designed to streamline document analysis, auditing, and review processes. This tool allows users to open text-based PDF documents, navigate through pages seamlessly, extract specific text snippets, append custom annotations or notes, and export the structured data directly into a formatted Excel spreadsheet.

## Key Features

* PDF Visualization & Navigation:
  - Clean, page-by-page text rendering via an intuitive graphical user interface (GUI).
  - Flexible navigation controls including Previous Page, Next Page, and Go to Page functionality.
* Interactive Text Capture:
  - Direct selection of text segments from the displayed PDF page content.
  - Dedicated metadata logging that automatically pairs each extraction with its corresponding page number.
* Structured Annotations:
  - Interactive entry field to append custom notes, descriptions, or comments against every captured snippet.
  - Real-time tabular data view summarizing all active selections within the current session.
* Automated Excel Export:
  - One-click data compilation exporting Page Numbers, Extracted Text, and User Notes into a clean .xlsx spreadsheet.
  - Smart file naming convention that automatically saves output files matching the source layout: <original_pdf_name>_selections.xlsx.
* Keyboard Shortcuts: Built-in key bindings optimized for rapid, mouse-free navigation and capture.

## Built With

* Python 3.x - Core application logic and execution.
* Tkinter - Native Desktop Graphical User Interface (GUI) development.
* pdfplumber - Robust, high-fidelity text extraction from PDF layouts.
* Pandas - High-performance structural data handling and tabular formatting.
* OpenPyXL - Engine for custom Excel spreadsheet compilation.
* PyInstaller - Standalone production executable packaging.

## Deliverables & Repository Structure

The project repository includes the following primary artifacts:
* pdf_text_selector_gui_cleaned.py: Fully documented, modular Python source code.
* requirements.txt: Python dependencies file for quick configuration.

---

## Workflow & Architecture

[ Open PDF ] ---> [ Extract & Display Text ] ---> [ Navigate & Select Text ]
                                                          |
[ Structured Excel Export ] <--- [ Tabular Summary ] <----+ [ Append Custom Note ]

1. Ingest: The user loads a text-based PDF file via the standard file-picker menu.
2. Render: The engine extracts and displays text dynamically for the current active page.
3. Capture: The user highlights a critical string of text, adds a review or audit note, and logs it.
4. Compile: Active selections are accumulated globally across any number of pages inside a structured data frame.
5. Output: The data structure is written to an automated Excel matrix with predefined column tracking.

---

## Getting Started

### Option A: Running from Source Code
To set up, configure, and execute the application locally from the Python source, follow these steps:

1. Clone or download the repository files into a folder.
2. Open your command prompt (cmd) or terminal and navigate to the project folder.
3. Set up a clean virtual environment (Recommended):
   python -m venv venv
   
   # Execution command on Windows to activate:
   venv\Scripts\activate
   
   # Execution command on macOS/Linux to activate:
   source venv/bin/activate

4. Install all required dependencies using the requirements file:
   pip install -r requirements.txt

5. Launch the application UI:
   python pdf_text_selector_gui_cleaned.py

---

## Output Schema

The compiled Excel document matches corporate tracking requirements with the following standardized structural schema:

* Page Number: [Integer] The exact source page where the text snippet was extracted.
* Selected Text: [String] The raw, unmodified text selection captured from the PDF document.
* User Notes: [String] Contextual remarks, calculations, or audit observations added by the reviewer.

---

## Professional & Business Impact

This application is designed to act as a productivity force-multiplier for analytical business units. Manual data copy-pasting during document compliance verification is a historical bottleneck. 

By utilizing this tool, professionals can systematically expedite critical workflows including:
* Bid & Proposal Reviews: Speed up technical specifications parsing and estimation workflows during tight tender timelines.
* Contractual Auditing: Seamlessly trace clauses, risk parameters, and financial compliance metrics down to the page level.
* Document Analysis: Convert dense, unstructured enterprise PDFs into actionable, tabular data assets optimized for executive reporting and downstream database management.
