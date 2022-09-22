import re


def has_integer(txtstr):
    tester = re.search('\d+ ', txtstr)
    # \d+ with space afterwords will
    # eliminate any character after a digit in the regex search

    if tester:
        print("Integer exists here")
    else:
        print("no integer")


floatstuff = '[+-]?([0-9]*[.])[0-9]+'  # float (consists of 1 or more digits before and after decimal point)


def has_float(txtstr):
    tester = re.search(floatstuff, txtstr)

    if tester:
        print("float exists here")
    else:
        print("no floating numbers")


float_two_num = '[+-]?([0-9]*[.])[0-9][0-9]$'


# A float with exactly 2 digits after the decimal point

def has_float_two_num(txtstr):
    tester = re.search(floatstuff, txtstr)

    if tester:
        print("float with 2 digits after decimal exists here")
    else:
        print("float with 2 digital after decimal does not exist here")


c_stringer = '[A-Z]+[a-z]+$|[A-Z]+[a-z]+[0-9]+$'


def has_cap(txtstr):
    tester = re.search(c_stringer, txtstr)

    if tester:
        print("Capital Letter + Lowercase + maybe digits here")
    else:
        print("No Capital Letter + Lowercase + maybe digits here")


triple_digi_plus_letter = '[0-9][0-9][0-9][a-z][a-z]+'


def has_tripdigitsandlets(txtstr):
    tester = re.search(triple_digi_plus_letter, txtstr, re.IGNORECASE)

    if tester:
        print("3 digits + 2+ letters here")
    else:
        print("No 3 digits + 2+ letters here")

# [“22.11”,“23”,“66.7f”, “123abcde”,“Case44”, “Happy”,”78”, “66.7”, “yes123”,”Book111”


