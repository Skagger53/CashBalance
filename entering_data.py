if __name__ == "__main__": print("This is a supporting module. Do not execute this directly.")
else:
    import misc_functions as mf
    import datetime

    def enter_dates(text):
        user_input_date = input(text)
        if len(user_input_date) == 0:
            mf.invalid_input("Please enter a date in the proper format (m/d/yyyy).\n")
            return False
        if user_input_date.strip().lower() == "back": return "back"
        try: user_input_date = datetime.datetime.strptime(user_input_date, "%m/%d/%Y")
        except ValueError:
            mf.invalid_input("Please enter a date in the proper format (m/d/yyyy).\n")
            return False
        return user_input_date

    def enter_starting_amount():
        starting_amount = False
        while starting_amount == False:
            starting_amount = mf.validate_input_float(input('Enter total cash starting amount. Type "back" to go back.\n'))
            if starting_amount == "back": return "back"
            return starting_amount

    def enter_full_cash():
        cash = False
        while cash == False:
            cash = input('Enter full cash amount. Type "back" to go back.\n')
            if cash == "back": return "back"
            if len(cash) == 0:
                mf.invalid_input("Please enter a number amount for the cash.")
                cash = False
            else:
                try: cash = float(cash)
                except ValueError:
                    mf.invalid_input("Please enter a number amount for the cash.")
                    cash = False
                else:
                    return cash

    def enter_cash_menu():
        enter_cash_input = False
        while enter_cash_input == False:
            print("1. Enter total cash value\n2. Enter number of individual denominations\n3. Back")
            enter_cash_input = mf.validate_input_tuple(input(), (1, 2, 3))
            if enter_cash_input == 1:
                cash = enter_full_cash()
                if cash == "back": enter_cash_input = False
                else: return cash
            if enter_cash_input == 2:
                cash = enter_denominations()
                if cash == "back": enter_cash_input = False
                else: return cash
            if enter_cash_input == 3: return "back"

    def enter_denominations():
        denominations = {"twenties": None, "tens": None, "fives": None, "ones": None, "quarters": None, "dimes": None, "nickels": None, "pennies": None, "all other types of denominations combined": None}
        i = 0
        while i < 9 and denominations[list(denominations.keys())[i]] == None:
            if i != 8: denominations[list(denominations.keys())[i]] = mf.validate_input_int(input(f'Enter the number of {list(denominations.keys())[i]} (or type "back"):\n'))
            else: denominations[list(denominations.keys())[i]] = mf.validate_input_float(input(f'Enter the number of {list(denominations.keys())[i]} (or type "back"):\n'))
            if denominations[list(denominations.keys())[i]] == "back" and i == 0: return "back"
            if denominations[list(denominations.keys())[i]] == "back":
                denominations[list(denominations.keys())[i - 1]], denominations[list(denominations.keys())[i]] = None, None
                i -= 1
            elif denominations[list(denominations.keys())[i]] != None: i += 1

        denominations_vals = [20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]
        total = 0
        for i in range(0, 8): total += denominations[list(denominations.keys())[i]] * denominations_vals[i]
        total += denominations["all other types of denominations combined"]
        return total

    def enter_comments():
        enter_comments_input = False
        while enter_comments_input == False:
            comments = input('Type your comments below. Type "back" to return to the previous menu without entering comments.\n')
            if len(comments) != 0:
                if comments.strip().lower() == "back":
                    return None
                elif len(comments) > 900:
                    mf.invalid_input("\nComments can not be longer than 900 characters. Please enter fewer comments.\nYou may want to copy your above comments before continuing.")
                else: enter_comments_input = True
        return comments