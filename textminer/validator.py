import re


def binary(test_string):
    return re.search(r'^[01]+$', test_string)


def binary_even(test_string):
    return re.search(r'^[01]*0$', test_string)


def hex(test_string):
    return re.search(r'^[0-9A-F]+$', test_string)


def word(test_string):
    return re.search(r'^[A-Za-z0-9/-]+[A-Za-z]$', test_string)


def words(test_string, count=0):
    if count:
        count -=1
    else:
        count = "0,"
    print(r'^([A-Za-z0-9/-]+[A-Za-z] ?){}([A-Za-z0-9/-]+[A-Za-z])$'.format("{"+str((count))+"}"))
    return re.search(r'^([A-Za-z0-9/-]+[A-Za-z] ){}([A-Za-z0-9/-]+[A-Za-z])$'.format("{"+str((count))+"}"), test_string)


def phone_number(test_string):
    return re.search(r'^((\(?[(0-9)]\)?){3}.?){1,2}\(?([0-9]){4}\)?$', test_string)


def money(test_string):
    return re.search(r'^\$[0-9][0-9,]*(\.[0-9]{2})?$', test_string)


if __name__ == "__main__":
    assert money("$4")
    assert money("$19")
    assert money("$19.00")
    assert money("$3.58")
    assert money("$1000")
    assert money("$1000.00")
    assert money("$1,000")
    assert money("$1,000.00")
    assert money("$5,555,555")
    assert money("$5,555,555.55")
    assert money("$45,555,555.55")
    assert money("$456,555,555.55")
    assert money("$1234567.89")
    assert not money("")
    assert not money("$12,34")
    assert not money("$1234.9")
    assert not money("$1234.999")
    assert not money("$")
    assert not money("31")
    assert not money("$$31")