# Return GTIN-13 product code check digit
def validate_gtin13_barcode_check_digit(gtin):

    total = 0

    for position,digit in enumerate(gtin):
        num_digit = int(digit)
        # Multiply every 2nd digit by 3
        if position % 2 == 0:           
            total += (num_digit*3)
        # Multiply other digits by 1
        else:
            total += num_digit

        if position == 11:
            additional_digit = total % 10
            return (10-additional_digit+num_digit)%10

# print(validate_gtin13_barcode_check_digit('9400550619779'))



# Return GTIN-13 product code check digit
def calculate_gtin13_barcode_check_digit(gtin):

    total = 0

    for position,digit in enumerate(gtin):
        num_digit = int(digit)
        # Multiply every 2nd digit by 3
        if position % 2 != 0:           
            total += (num_digit*3)
        # Multiply other digits by 1
        else:
            total += num_digit

        if position == 12:
            additional_digit = total % 10
            if additional_digit == 0:
                return('This is a valid gtin13 barcode.')
            # correct value of check digit
            else:
                return (10-additional_digit+num_digit)%10

# print(calculate_gtin13_barcode_check_digit('9400550619779'))
