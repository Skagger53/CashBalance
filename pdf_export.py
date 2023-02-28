if __name__ == "__main__":
    input("This is a supporting module. Do not execute this directly.\n\nTerminating.\n")

    import sys
    sys.exit()

from fpdf import FPDF
import datetime

def create_pdf(date_range, record_total, starting_amount, cash_on_hand, comments, path):
    pdf_export = FPDF("P", "in", "Letter")
    pdf_export.add_page()
    pdf_export.set_font("helvetica", "I", 18)

    pdf_export.image("logo.png", 2.5, .75, 3.5)
    pdf_export.set_y(2.6)
    pdf_export.multi_cell(w=0, h=.3, txt="The Estates at Chateau:\nCash-on-hand reconciliation\nfor RFMS Resident Trust Funds", align="C")

    pdf_export.set_line_width(.02)
    pdf_export.line(1.25, 3.75, 7, 3.75)

    pdf_export.set_xy(1, 4)
    pdf_export.set_font("helvetica", "", 11)
    pdf_export.cell(w = 0, h = .25, txt = f"Cash withdrawal date range: {date_range[0].strftime('%#m/%#d/%Y')} to {date_range[1].strftime('%#m/%#d/%Y')}")

    pdf_export.set_xy(1, 4.45)
    pdf_export.multi_cell(w=0, h=.2, txt=f"Starting balance: ${'{:.2f}'.format(starting_amount)}\nRFMS cash withdrawals recorded: ${'{:.2f}'.format(record_total)}\nCash predicted to be on hand: ${'{:.2f}'.format(starting_amount - record_total)}\nActual cash on hand: ${'{:.2f}'.format(cash_on_hand)}", align="L")
    pdf_export.set_font("helvetica", "BU", 11)
    pdf_export.set_x(1)
    difference = round(cash_on_hand - (starting_amount - record_total), 2) # Rounding to avoid floating point errors
    if difference == 0: difference = 0 # This looks unneeded, but without this line, a balanced reconciliation may display a difference of "$-0.00" due to a floating point error.
    pdf_export.cell(w = 0, h = .2, txt = f"Difference: ${'{:.2f}'.format(difference)}")

    pdf_export.set_font("helvetica", "", 11)

    if comments != None:
        pdf_export.set_xy(1, 5.75)
        pdf_export.multi_cell(w = 6.25, h = .2, txt = f"Comments: {comments}")

        pdf_export.set_xy(1, 8.5)
        pdf_export.cell(w=0, h=.2, txt=f"Date printed: {datetime.date.today().strftime('%#m/%#d/%Y')}")

        pdf_export.set_font("helvetica", "I", 7)
        pdf_export.set_line_width(.01)
        pdf_export.line(1.05, 9.25, 3.6, 9.25)
        pdf_export.line(4.7, 9.25, 7.25, 9.25)
        pdf_export.set_xy(1, 9.3)
        pdf_export.cell(w = 0, h = .2, txt = "Administrator name (printed)")
        pdf_export.set_xy(1, 9.95)
        pdf_export.cell(w=0, h=.2, txt="Administrator signature")

        pdf_export.line(1.05, 9.9, 3.6, 9.9)
        pdf_export.line(4.7, 9.9, 7.25, 9.9)
        pdf_export.set_xy(4.65, 9.3)
        pdf_export.cell(w=0, h=.2, txt="Business Office Manager name (printed)")
        pdf_export.set_xy(4.65, 9.95)
        pdf_export.cell(w=0, h=.2, txt="Business Office Manager signature")

        pdf_export.output(f"{path}EAC_RFMS_Reconciliation_{date_range[0].strftime('%m-%d-%Y')}_to_{date_range[1].strftime('%m-%d-%Y')}.pdf")
    else:
        pdf_export.set_xy(1, 6)
        pdf_export.cell(w=0, h=.2, txt=f"Date printed: {datetime.date.today().strftime('%#m/%#d/%Y')}")

        pdf_export.set_font("helvetica", "I", 7)
        pdf_export.set_line_width(.01)
        pdf_export.line(1.05, 6.75, 3.6, 6.75)
        pdf_export.line(4.7, 6.75, 7.25, 6.75)
        pdf_export.set_xy(1, 6.8)
        pdf_export.cell(w=0, h=.2, txt="Administrator name (printed)")
        pdf_export.set_xy(1, 7.45)
        pdf_export.cell(w=0, h=.2, txt="Administrator signature")

        pdf_export.line(1.05, 7.4, 3.6, 7.4)
        pdf_export.line(4.7, 7.4, 7.25, 7.4)
        pdf_export.set_xy(4.65, 6.8)
        pdf_export.cell(w=0, h=.2, txt="Business Office Manager name (printed)")
        pdf_export.set_xy(4.65, 7.45)
        pdf_export.cell(w=0, h=.2, txt="Business Office Manager signature")

        #path = path.replace('/', '\\')
        pdf_export.output(f"{path}EAC_RFMS_Reconciliation_{date_range[0].strftime('%m-%d-%Y')}_to_{date_range[1].strftime('%m-%d-%Y')}.pdf")