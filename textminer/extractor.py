import re


def phone_numbers(test_string):
    return re.findall(r'\(\d{3}\) \d{3}-\d{4}', test_string)
