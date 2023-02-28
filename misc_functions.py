if __name__ == "__main__":
    input("This is a supporting module. Do not execute this directly.\n\nTerminating.\n")

    import sys
    sys.exit()

def invalid_input(text):
    print(f"{text}\n\n(Press enter.)")
    input()

def validate_input_int(user_input):
    invalid_message = "Please enter a whole number."
    if user_input.strip().lower() == "back": return "back"
    if len(user_input) == 0:
        invalid_input(invalid_message)
        return False
    else:
        try: user_input = int(user_input)
        except ValueError:
            invalid_input(invalid_message)
            return False
        if user_input < 0:
            invalid_input(invalid_message)
            return False
        return user_input

def validate_input_tuple(user_input, tuple):
    invalid_message = f"Please enter a number between {tuple[0]} and {tuple[-1]}."
    if len(user_input) == 0 or len(user_input) > 2:
        invalid_input(invalid_message)
        return False
    else:
        try: user_input = int(user_input)
        except ValueError:
            invalid_input(invalid_message)
            return False
        if user_input not in tuple:
            invalid_input(invalid_message)
            return False
        return user_input

def validate_input_float(user_input):
    if len(user_input) == 0:
        invalid_input("Please enter a number.")
        return False
    if user_input.strip().lower() == "back": return "back"
    try: user_input = float(user_input)
    except ValueError:
        invalid_input("Please enter a number")
        return False
    return user_input

def input_y_n(text):
    user_input = False
    while user_input == False:
        user_input = input(f"{text} Enter y/n.\n")
        if len(user_input) == 0: invalid_input("Please enter y/n.")
        else:
            if len(user_input.strip()) == 1:
                if user_input.strip().lower() == "y": return True
                if user_input.strip().lower() == "n": return False
            if user_input.strip().lower() == "yes": return True
            if user_input.strip().lower() == "no": return False
            invalid_input("Please enter y/n.")

def display_entered_info(date_range, starting_amount, record_total, cash_on_hand):
    overview = []
    if date_range != None: overview.append(f"Dates: {date_range[0].strftime('%#m/%#d/%Y')} to {date_range[1].strftime('%#m/%#d/%Y')}")
    if starting_amount != None: overview.append(f"Starting amount: ${'{:.2f}'.format(starting_amount)}")
    if record_total != None: overview.append(f"RFMS Withdrawal Record Total: ${'{:.2f}'.format(record_total)}")
    if record_total != None and starting_amount != None: overview.append(f"Predicted cash on hand: ${'{:.2f}'.format(starting_amount - record_total)}")
    if cash_on_hand != None: overview.append(f"Cash on hand: ${'{:.2f}'.format(cash_on_hand)}")
    return overview
