if __name__ == "__main__":
    input("This is a supporting module. Do not execute this directly.\n\nTerminating.\n")

    import sys
    sys.exit()

import PyPDF2
from tkinter import filedialog
import misc_functions as mf

def validate_extract_pdf(path):
    invalid_file_message = "Please select a valid RFMS Withdrawal Record PDF.\n"
    if path[-4:].lower() != ".pdf":
        mf.invalid_input(invalid_file_message)
        return False
    pdf_doc = PyPDF2.PdfReader(path)
    pdf_doc_num_pages = len(pdf_doc.pages)
    if pdf_doc.metadata.title != "Withdrawal Record":
        mf.invalid_input(invalid_file_message)
        return False
    if pdf_doc_num_pages == 0:
        mf.invalid_input(invalid_file_message)
        return False

    full_pdf_text = []
    for page in range(0, pdf_doc_num_pages): full_pdf_text.append(pdf_doc.pages[page].extract_text().split("\n"))
    for page in full_pdf_text:
        if page[4] != "Withdrawal Record" or page[6][:13] != "Facility ID #":
            print("withdrawal record/facility ID")
            mf.invalid_input(invalid_file_message)
            return False

    total_record_cash = 0
    for page in full_pdf_text:
        for i, line in enumerate(page):
            if line == "RESIDNT ADVANCE " and page[i + 2] == "CASH": total_record_cash += float(page[i - 2].replace(",", ""))

    return total_record_cash

def get_pdf():
    pdf_path = filedialog.askopenfilename(initialdir="/", title="Select RFMS Withdrawal Record", filetypes=(("PDF files", "*.pdf"), ("all files", "*.*")))
    pdf_doc = validate_extract_pdf(pdf_path)
    if pdf_doc == False: return None, None
    return pdf_doc, pdf_path[:pdf_path.rfind("/") + 1]
