if __name__ != "__main__": print("This is the main module. Do not call this module.")
else:
    import misc_functions as mf
    import pdf_import as pim
    import entering_data as ed
    import pdf_export as pe

    def menu_one():
        date_range = None
        comments = None
        cash_on_hand = None
        starting_amount = None
        menu_one_input = False
        record_total = None
        starting_date = False
        while menu_one_input == False:
            header = mf.display_entered_info(date_range, starting_amount, record_total, cash_on_hand)
            if header != []:
                for item in header: print(item)
            print("1. Enter date range\n2. Select RFMS Withdrawal Record\n3. Enter starting amount\n4. Enter cash on hand\n5. Enter comments\n6. View comments\n7. Export PDF\n8. Quit")
            menu_one_input = mf.validate_input_tuple(input(), range(1, 9))

            match menu_one_input:
                case 1:
                    starting_date = False
                    while starting_date == False:
                        starting_date = ed.enter_dates('Enter the starting date in the format of m/d/yyyy (or type "back"):')
                        if starting_date == "back": menu_one_input = False
                        elif starting_date != False:
                            ending_date = False
                            while ending_date == False:
                                ending_date = ed.enter_dates('Enter the ending date in the format of m/d/yyyy (or type "back"):')
                                if ending_date == "back": starting_date = False
                                elif ending_date != False:
                                    if starting_date <= ending_date:
                                        menu_one_input = False
                                        date_range = (starting_date, ending_date)
                                    else:
                                        mf.invalid_input("You have entered a starting date that is after your ending date. Please enter the date range again.")
                                        starting_date = False

                case 2:
                    if record_total != None:
                        if mf.input_y_n( f"You have already loaded an RFMS Withdrawal Record (which totaled ${'{:.2f}'.format(record_total)}. Do you want to select a new record and overwrite this one?\n") == True:
                            menu_one_input = False
                            record_total, path = pim.get_pdf()
                        else: menu_one_input = False
                    else:
                        menu_one_input = False
                        record_total, path = pim.get_pdf()

                case 3:
                    if starting_amount != None:
                        if mf.input_y_n((f"You have already entered a starting amount of ${'{:.2f}'.format(starting_amount)}. Do you want to enter a new amount?\n")) == True:
                            prev_starting_amount = starting_amount
                            menu_one_input, starting_amount = False, ed.enter_starting_amount()
                            if starting_amount == "back": starting_amount = prev_starting_amount
                        else: menu_one_input = False
                    else: menu_one_input, starting_amount = False, ed.enter_starting_amount()
                    if starting_amount == "back": menu_one_input, starting_amount = False, None

                case 4:
                    if cash_on_hand != None:
                        if mf.input_y_n(f"You have already entered cash on hand as ${'{:.2f}'.format(cash_on_hand)}. Do you want to enter a new amount?\n") == True:
                            prev_cash_on_hand = cash_on_hand
                            menu_one_input, cash_on_hand = False, ed.enter_cash_menu()
                            if cash_on_hand == "back": cash_on_hand = prev_cash_on_hand
                        else: menu_one_input = False
                    else: menu_one_input, cash_on_hand = False, ed.enter_cash_menu()
                    if cash_on_hand == "back": menu_one_input, cash = False, None

                case 5:
                    if comments != None:
                        comments_proceed = mf.input_y_n("Entering new comments will delete your old comments. Proceed?")
                        if comments_proceed == True: menu_one_input, comments = False, ed.enter_comments()
                        else: menu_one_input = False
                    else: menu_one_input, comments = False, ed.enter_comments()

                case 6:
                    if comments == None:
                        input("No comments have been entered yet.")
                        menu_one_input = False
                    else:
                        input(f"Comments:\n\n{comments}\n\n(Press enter.)")
                        menu_one_input = False

                case 7:
                    missing_data = []
                    if starting_date == False: missing_data.append("date range")
                    if cash_on_hand == None: missing_data.append("cash on hand")
                    if starting_amount == None: missing_data.append("starting amount")
                    if record_total == None: missing_data.append("RFMS Withdrawal Record")
                    if comments == None and round(starting_amount - record_total, 2) != cash_on_hand: missing_data.append("comments (REQUIRED due to cash on hand not equalling predicted cash amount)") # Rounding to avoid floating point errors
                    if len(missing_data) > 0:
                        input(f"You must provide the following data before you can export to PDF: {', '.join(missing_data)}\n(Press enter.)\n")
                        menu_one_input = False
                    else:
                        if comments == None:
                            if mf.input_y_n("You have not entered any comments. Do you want to enter comments before generating the PDF?") == True: menu_one_input, comments = False, ed.enter_comments()
                            else:
                                pe.create_pdf(date_range, record_total, starting_amount, cash_on_hand, comments, path)
                                input("PDF created!\n(Press enter.)")
                                menu_one_input = False
                        else:
                            pe.create_pdf(date_range, record_total, starting_amount, cash_on_hand, comments, path)
                            input("PDF created!\n(Press enter.)")
                            menu_one_input = False


                case 8:
                    if mf.input_y_n("Are you sure you want to quit?") == False: menu_one_input = False

    menu_one()