# ~/Documents/SheCodes/Python1Task/shecodes-week-5-task-1

# Algorithms to calculate and validate check digits for different kinds of barcodes.

# Credit Cards
def validate_credit_card_barcode_check_digit(card_no):
    total = 0
    for position,digit in enumerate(card_no[::-1]):
        num_digit = int(digit)
        if position % 2 != 0:
            multiply_digit_2 = num_digit*2
            str_multiply_digit_2 = str(multiply_digit_2)
            if multiply_digit_2 > 9:
                subtotal = 0
                for second_digit in str_multiply_digit_2:
                    num_second_digit = int(second_digit)
                    subtotal += num_second_digit
                total += subtotal
            else:
                total += multiply_digit_2
        else:
            total += num_digit
        if position == len(card_no)-1:
            sum = total * 9
            if sum % 10 == 0:
                return ('This is a valid credit card number.')
            else:
                return ('This is an invalid credit card number.')

# print(validate_credit_card_barcode_check_digit('4111111111111111'))


# Credit Cards
def calculate_credit_card_barcode_check_digit(card_no):
    total = 0
    for position,digit in enumerate(card_no[::-1]):
        num_digit = int(digit)
        if position % 2 == 0:
            multiply_digit_2 = num_digit*2
            str_multiply_digit_2 = str(multiply_digit_2)
            if multiply_digit_2 > 9:
                subtotal = 0
                for second_digit in str_multiply_digit_2:
                    num_second_digit = int(second_digit)
                    subtotal += num_second_digit
                total += subtotal
            else:
                total += multiply_digit_2
        else:
            total += num_digit
        if position == len(card_no)-1:
            sum = total * 9
            return (str(sum)[-1:])

# print(calculate_credit_card_barcode_check_digit('5499740000000057'))