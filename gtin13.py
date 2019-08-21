def validate_gtin13_barcode_check_digit(gtin):

    total = 0

    for position,digit in enumerate(gtin):
        num_digit = int(digit)
        # multiply every 2nd digit by 3
        if position % 2 != 0:           
            total += (num_digit*3)
        # multiply other digits by 1
        else:
            total += num_digit
        # perform check if it is the last digit
        if position == 12:
            additional_digit = total % 10
            if additional_digit == 0:
                return('This is a valid gtin13 barcode.')
            else:
                return ('This is an invalid gtin13 barcode.')

# print(validate_gtin13_barcode_check_digit('940055061977'))


def calculate_gtin13_barcode_check_digit(gtin):

    total = 0

    for position,digit in enumerate(gtin):
        num_digit = int(digit)
        # multiply every 2nd digit by 3
        if position % 2 != 0:           
            total += (num_digit*3)
        # multiply other digits by 1
        else:
            total += num_digit
        # perform check if it is the last digit
        if position == 11:
            additional_digit = total % 10
            if additional_digit == 0:
                return '0'
            else:
                return str(10-additional_digit)

# print(calculate_gtin13_barcode_check_digit('940055061977'))
