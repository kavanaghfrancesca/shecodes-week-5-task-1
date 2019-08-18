def calculate_isbn13_barcode_check_digit(isbn):

    total = 0

    for position,digit in enumerate(isbn):
        num_digit = int(digit)
        # 1st = multiply by 1, 2nd = multiply by 3, 3rd = 1..etc and sum total
        if position % 2 != 0:            
            total += (num_digit*3)
        else:
            total += num_digit
        remainder = total % 10
        # perform check once last digit reached
        if position == 11:
            return str(10 - (total % 10))

# print(calculate_isbn13_barcode_check_digit('978071485726'))

def validate_isbn13_barcode_check_digit(isbn):

    total = 0

    for position,digit in enumerate(isbn):
        num_digit = int(digit)
        # Only sum first 12 digits of the 13-digit ISBN
        if position == 12:
            pass
        # 1st = multiply by 1, 2nd = multiply by 3, 3rd = 1..etc and sum total
        elif position % 2 != 0:            
            total += (num_digit*3)
        else:
            total += num_digit
        remainder = total % 10
        # perform check once last digit reached
        if position == 12:
            # valid if 0 and last digit 0 
              if num_digit == 0 and remainder == 0:
                  return('This is a valid isbn13 barcode.')
            # valid if 10 - remainder equals the last digit of 13-digit ISBN
              elif 10-remainder == num_digit:
                  return('This is a valid isbn13 barcode.')
            # return value it is supposed to be
              else:
                  return('This is an invalid isbn13 barcode.')

# print(validate_isbn13_barcode_check_digit('9781742660461'))
