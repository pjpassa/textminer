import re


def binary(test_string):
    return re.match(r'[01]', test_string)


def binary_even(test_string):
    return re.search(r'^[01]*0$', test_string)


def hex(test_string):
    return re.search(r'^[\dA-F]+$', test_string)


def word(test_string):
    return re.search(r'^[A-Za-z\d/-]+[A-Za-z]$', test_string)


def words(test_string, count=0):
    if count:
        count -= 1
    else:
        count = "0,"
    print(r'^([A-Za-z\d/-]+[A-Za-z] ?){}([A-Za-z\d/-]+[A-Za-z])$'.format("{"+str((count))+"}"))
    return re.search(r'^([A-Za-z\d/-]+[A-Za-z] ){}([A-Za-z\d/-]+[A-Za-z])$'.format("{"+str((count))+"}"), test_string)


def phone_number(test_string):
    return re.search(r'^((\(?[(\d)]\)?){3}.?){1,2}\(?([\d]){4}\)?$', test_string)


def money(test_string):
    if "," in test_string:
        return re.search(r'^\$(\d{0,3})?(,\d{3})*(\.\d{2})?$', test_string)
    return re.search(r'^\$\d+(\.\d{2})?$', test_string)


def zipcode(test_string):
    return re.search(r'^\d{5}(-\d{4})?$', test_string)


def date(test_string):
    return re.search(r'^(\d{1,4}[/-]){2}\d{1,4}$', test_string)
