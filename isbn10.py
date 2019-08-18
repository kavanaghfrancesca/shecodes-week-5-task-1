# ISBN-10 Books
def calculate_isbn10_barcode_check_digit(isbn):

    total = 0

    for position, digit in enumerate(isbn):
        num_digit = int(digit)
        #Multiply first digit by 10, second by 9..etc
        total += (num_digit*(len(isbn)-position))
    #return X if check digit is 10
    if total % 11 == 10 or total % 11 == 0:
        return('This is a valid isbn10 barcode.')
    else:
        return(11 - (total % 11))

# print(calculate_isbn10_barcode_check_digit('0205080057'))
