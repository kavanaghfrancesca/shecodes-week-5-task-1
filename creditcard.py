def calculate_credit_card_number_check_digit(card_no):
    total = 0
    # start from last digit from credit card number
    for position,digit in enumerate(card_no[::-1]):
        num_digit = int(digit)
        # position is even as credit card digit has a missing number
        if position % 2 == 0:
            multiply_digit_2 = num_digit*2
            str_multiply_digit_2 = str(multiply_digit_2)
            if multiply_digit_2 > 9:
                subtotal = 0
                # loop through 2 digits to get subtotal to add to total
                for second_digit in str_multiply_digit_2:
                    num_second_digit = int(second_digit)
                    subtotal += num_second_digit
                total += subtotal
            # add 2*digit for every other digit from the digit after check
            else:
                total += multiply_digit_2
        # add digit for every other digit from check
        else:
            total += num_digit
        #formula to calculate check digit
        if position == len(card_no)-1:
            sum = total * 9
            return (str(sum)[-1:])

# print(calculate_credit_card_number_check_digit('542418027979176'))


def validate_credit_card_number_check_digit(card_no):
    total = 0
    # start from last digit from credit card number
    for position,digit in enumerate(card_no[::-1]):
        num_digit = int(digit)
        # position is even as credit card digit has a missing number
        if position % 2 != 0:
            multiply_digit_2 = num_digit*2
            str_multiply_digit_2 = str(multiply_digit_2)
            if multiply_digit_2 > 9:
                subtotal = 0
                # loop through 2 digits to get subtotal to add to total
                for second_digit in str_multiply_digit_2:
                    num_second_digit = int(second_digit)
                    subtotal += num_second_digit
                total += subtotal
            # add 2*digit for every other digit from the digit after check
            else:
                total += multiply_digit_2
        # add digit for every other digit from check
        else:
            total += num_digit
        #formula to calculate check digit
        if position == len(card_no)-1:
            sum = total * 9
            if sum % 10 == 0:
                return ('This is a valid credit card number.')
            else:
                return ('This is an invalid credit card number.')

# print(validate_credit_card_number_check_digit('5424180279791762'))