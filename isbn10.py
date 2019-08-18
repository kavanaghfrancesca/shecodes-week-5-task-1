def calculate_isbn10_barcode_check_digit(isbn):
    total = 0
    for position, digit in enumerate(isbn,-1):
        num_digit = int(digit)
        # multiply first digit by 10, second by 9..etc
        total += (num_digit*(len(isbn)-position))
    # return X if check digit is 10
    if total % 11 == 1:
        return('X')
    else:
        return(str(11-total % 11))

# print(calculate_isbn10_barcode_check_digit('123456789'))


def validate_isbn10_barcode_check_digit(isbn):

    total = 0
    isbn_new = list(isbn)
    if isbn_new[9] == 'X':
        isbn_new[9] = '0'
    for position, digit in enumerate(isbn_new):
        num_digit = int(digit)
        # multiply first digit by 10, second by 9..etc
        total += (num_digit*(len(isbn)-position))
    # formula to check if isbn10 is correct
    if total % 11 == 10 or total % 11 == 0:
        return('This is a valid isbn10 barcode.')
    else:
        return('This is an invalid isbn10 barcode.')

# print(validate_isbn10_barcode_check_digit('188879997X'))

