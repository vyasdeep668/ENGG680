# Course: ENGG 680 Intro to Digital Engineering
# Assignment #: 1
# Topic: Credit card number check (1pt)
# Name: Deep Vyas
# UCID: 30139014

import re


def check(card_number):
    """
    Name: check(card_number)
    Description: 1. If the string does not follow the format "dddd dddd dddd dddd", where each d is a digit,
                    it should return False.
                 2. If the sum of the digits is divisible by 10 (a "checksum" method), then the procedure
                    should return True, otherwise it should return False. For example, if card_number is the string
                    "9384 3495 3297 0123" then although the format is correct, the digit’s sum is 72 so you should
                    return False
    Input: card_number
    Output: True/False
    """

    # Input format check
    str_format = "[0-9][0-9][0-9][0-9] [0-9][0-9][0-9][0-9] [0-9][0-9][0-9][0-9] [0-9][0-9][0-9][0-9]"
    if not bool(re.match(str_format, card_number)):
        return False

    # Sum of digits check
    card_number = card_number.replace(" ", "")  # Remove spaces
    digit_sum = 0
    for digit in card_number:
        digit_sum = digit_sum + int(digit)
    if not digit_sum % 10 == 0:
        return False

    return True


# Test Inputs
card_numbers = ["9384 3495 3297 0121",
                "9384 3495 3297 0123",
                "9384 3495 3297 01236",
                "9384 3495 3297 012A"]

print(card_numbers[0], check(card_numbers[0]))
print(card_numbers[1], check(card_numbers[1]))
print(card_numbers[2], check(card_numbers[2]))
print(card_numbers[3], check(card_numbers[3]))




