import re


def has_integer(txtstr):
    intstuff = '^[-+]?\d+$'
    tester = re.search(intstuff, txtstr)

    if tester:
        print("Integer exists here in " + txtstr)
    else:
        print("no integer in " + txtstr)


def has_float(txtstr):
    floatstuff = '[+-]?([0-9]*[.])[0-9]+'  # float (consists of 1 or more digits before and after decimal point)
    tester = re.search(floatstuff, txtstr)

    if tester:
        print("float exists here in " + txtstr)
    else:
        print("no floating numbers in " + txtstr)


# A float with exactly 2 digits after the decimal point

def has_float_two_num(txtstr):
    float_two_num = '[+-]?([0-9]*[.])[0-9][0-9]$'
    tester = re.search(float_two_num, txtstr)

    if tester:
        print("∃ float with 2 digits after decimal exists here in " + txtstr)
    else:
        print("no float with 2 digital after decimal here in " + txtstr)


def has_cap(txtstr):
    c_stringer = '[A-Z]+[a-z]+$|[A-Z]+[a-z]+[0-9]+$'
    tester = re.search(c_stringer, txtstr)

    if tester:
        print("Capital Letter + Lowercase + maybe digits here in " + txtstr)
    else:
        print("No Capital Letter + Lowercase + maybe digits here in " + txtstr)


def has_tripdigitsandlets(txtstr):
    triple_digi_plus_letter = '[0-9][0-9][0-9][a-z][a-z]+'
    tester = re.search(triple_digi_plus_letter, txtstr, re.IGNORECASE)

    if tester:
        print("3 digits + 2+ letters here in " + txtstr)
    else:
        print("No 3 digits + 2+ letters here in " + txtstr)


teststring = ["22.11", "23", "66.7f", "123abcde", "Case44", "Happy", "78", "66.7", "yes123", "Book111"]

for i in teststring:
    has_integer(i)
    has_float(i)
    has_float_two_num(i)
    has_cap(i)
    has_tripdigitsandlets(i)
    print('\n')