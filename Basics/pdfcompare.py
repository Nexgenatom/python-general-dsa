import os
import fitz  # PyMuPDF
import difflib
import csv

# Paths
EXPECTED_DIR = "H:\\PDFFiles\\ExpectedFiles"
ACTUAL_DIR = "H:\\PDFFiles\\ActualFiles"
OUTPUT_FILE = "H:/PDFFiles/Output/report.csv"

# Function to extract text from a PDF
def extract_text(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join(page.get_text("text") for page in doc)
        return text.strip()
    except Exception as e:
        return f"Error: {e}"

# Function to compare text using difflib
def compare_text(expected_text, actual_text):
    diff = difflib.ndiff(expected_text.split(), actual_text.split())
    changes = [line for line in diff if line.startswith('- ') or line.startswith('+ ')]
    return "PASS" if not changes else "FAIL"

# Function to compare all PDFs
def compare_pdfs():
    results = [["File Name", "Status"]]

    expected_files = {f for f in os.listdir(EXPECTED_DIR) if f.endswith(".pdf")}
    actual_files = {f for f in os.listdir(ACTUAL_DIR) if f.endswith(".pdf")}

    for file in expected_files:
        expected_path = os.path.join(EXPECTED_DIR, file)
        actual_path = os.path.join(ACTUAL_DIR, file)

        if file in actual_files:
            expected_text = extract_text(expected_path)
            actual_text = extract_text(actual_path)

            if "Error:" in expected_text or "Error:" in actual_text:
                results.append([file, "ERROR"])
            else:
                status = compare_text(expected_text, actual_text)
                results.append([file, status])
        else:
            results.append([file, "MISSING"])

    # Write results to CSV
    os.makedirs("output", exist_ok=True)
    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(results)

    print(f"Comparison Report Generated: {OUTPUT_FILE}")

# Run script
if __name__ == "__main__":
    compare_pdfs()
