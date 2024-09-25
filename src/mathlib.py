# TO convert decimal to binary
def dec_to_bin(number):
    result = ""
    q = int(number)

    # Convert base 10 to base 2 by division-remainder
    while q != 0 and q != 1:
        r = q % 2  # get the remainder
        result = result + str(r)  # include the remainder on the result
        q = int(q / 2)  # get the next number to be divided

    result = result + str(q)  # include the quotient on the result
    result_in_binary = result[::-1]  # reverse the result to get the converted number

    return int(result_in_binary)


# TO convert decimal to hexadecimal
def dec_to_hex(number):
    # Creating dictionary
    switch = {
        10: "a",
        11: "b",
        12: "c",
        13: "d",
        14: "e",
        15: "f",
    }

    result = ""
    q = int(number)

    # Convert base 10 to base 16 by division-remainder
    while q >= 16:
        r = q % 16  # get the remainder
        r = switch.get(r, r)  # convert if it's bigger than 10
        result = result + str(r)  # include the remainder on the result
        q = int(q / 16)  # get the next number to be divided

    q = switch.get(q, q)  # convert the last quotient
    result = result + str(q)  # include the quotient on the result
    result_in_hex = result[::-1]  # reverse the result to get the converted number

    return result_in_hex


# Recursive factorial function: calculates the n! by calling itself, since n! = n * (n - 1)!
def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number - 1)


# TO determinate if the number is odd or even
def is_it_odd(number):
    if (number % 2) == 0:
        return False
    else:
        return True


# TO determinate if the number is odd or even
def is_it_even(number):
    if (number % 2) == 0:
        return True
    else:
        return False


# TO convert a formatted number as a String into an integer
def str_to_int(number):
    # Splitting the integer and the decimal parts from the number
    parts = number.split(",")

    # Fix: giving a decimal number in case there isn't any
    if len(parts) > 1:
        part_dec = int("".join(parts[1]))
    else:
        part_dec = 00

    # Removing the periods (thousands separators) from the integer number
    part_int = int("".join(parts[0].split(".")))

    # Checking if it needs rounding up
    if part_dec > 50:
        part_int += 1

    return part_int


# TO convert an integer into a formatted number as a String
def int_to_str(number):
    reversed_number = str(number)[::-1]
    count = 0
    result = "00,"

    for digit in reversed_number:
        result = result + digit
        count += 1
        if count == 3:
            result = result + "."
            count = 0

    result = result[::-1]
    if result[0] == ".":
        result = result[1:]

    return result
