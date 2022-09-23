# Python exercise questions
# Help you getting familiar with Python syntax

# Grading:

# IMPORTANT NOTICE:
# A good practice in coding is to show your customer a working version and tell them
# what new features you want to add next.
# Thus, we require you to submit all your homework as a working version. If you
# only know how to solve 7/10 questions, just submit the 7 that runs without errors.
# For incomplete answers, comment the code out and print a line tell us your progress
# E.g. "Problem 3 is a completed but has run time errors"
# or "problem 5 is incomplete, but I did 75% of the work."

# Complete HW + correct results: 10pt
# Each question has a equal share of the total points
# Code that does not run will have only 2pt.
# No submission: 0%

# Please follow the required input/output and function names
# Main function is at the end of the file
# Please call all of your completed functions and print the results out

# Please define all the needed input variables in your main function directly and not asking for
# user input. Also, please format the output from each function and print them out in the main.

import random

'''
 1. Input: Count
 Output: print Count number of "hello":
            1th hello
           2th hello...
 IMPORTANT: copy to visualizer, observe the behavior
'''


def easy_hello_loop1_for(Count):
    for i in range(Count):
        print(str(i + 1) + "th hello")


'''
2.Input: number x,y
 Output: return the smaller value of the two
 Do it by yourself, no system calls like min()
'''


def smaller_value(x, y):
    if x < y:
        return x
    if y < x:
        return y
    else:
        print("both numbers have the same value")
    print('\n')


'''
3. Do not use len(). Write a function to calculate how many elements do you have in your list, and return it
'''


def my_len(lis):
    n = 0
    for i in lis:
        n = n + 1
    print("there are " + str(n) + " elements in this list")


'''
4. input: a list with small strings that has 2 letters, 3 letters, or 4 letters
output: return 3 lists, Letter2, Letter3, Letter4 containing small strings. Print results out in the main function.
Sample:
input list: ['rt','asdf','ton','er','user']
will give
    Letter2=['rt','er']
    Letter3=['ton']
    Letter4=['asdf','user']
You can use len() in this question.
'''


def cate_letters(LongStr):
    Letter2 = []
    Letter3 = []
    Letter4 = []
    for i in LongStr:
        if len(i) == 2:
            print("two here")
            Letter2.append(i)
        if len(i) == 3:
            print("three here")
            Letter3.append(i)
        if len(i) == 4:
            print("four here")
            Letter4.append(i)


'''
5. input: a string with letters in it, a string with numbers in it.
We assume they have same amount of characters/length. 
output: go through the two strings together, print out elements by index
format "the elements at index __ from string1 is __, from string2 is ___"
'''


def two_strings1(str1, str2):
    for i in range(len(str1)):
        print("elements at index " + str(i) + " from string1 is " + str1[i] + " from string2 is " + str2[i])


'''
6. input: a string with letters in it, a string with numbers in it
output: go through the two strings together. At index i, if the number in str2 is even, put the letter in str1 into evenStr
if the number is odd, put the letter into oddStr. Return the even/odd strings
Sample: "helloworld" "2435232399"
gives evenStr="heoo" oddStr="llwrld"
'''


def two_strings2(str1, str2):
    evenStr = ""
    oddStr = ""
    for i in range(len(str1)):
        if (int(str2[i]) % 2) == 0:
            print("hello " + str2[i])
            evenStr = evenStr + str1[i]
        else:
            print(str2[i])
            oddStr = oddStr + str1[i]

    print("evenStr=\"" + evenStr + "\"")
    print("evenStr=\"" + oddStr + "\"")


'''
7.
The number 6 is a truly great number. Given two int values, a and b, return True
if either one is 6. Or if their sum or difference is 6.
Note: the function abs(num) computes the absolute value of a number.

love6(6, 4) returns True
love6(4, 5) returns False
love6(1, 5) returns True
'''


def love6(a, b):
    if a == 6:
        print("true")
    elif b == 6:
        print("true")
    elif (abs(a + b)) == 6:
        print("true")
    elif (abs(a - b)) == 6:
        print("true")
    else:
        print("false")


'''
########
#8. ISBN number

#As you know, every book has an unique ISBN number (International Standard Book Number).
#It is a 10-digit (or 13) code that uniquely specifies a book. Since this number is long, the right most digit is actually a "checksum"
#to roughly check if all the digits are correct (not mis-typed etc.) and forming a legit ISBN number. (checksum is also used in other places, like credit card number.)
#The rule is: when adding all the (10 numbers * its position (rightmost be position 1, leftmost be 10)) together, the sum should be divisible by 11.
#For example: ISBN 020131452-5 is legit since:
#               (0*10 + 2*9 + 0*8 + 1*7 + 3*6 + 1*5 + 4*4 + 5*3 + 2*2 + 5*1)%11 = 88%11 = 0 the sum 88 is divisible by 11
#In fact, the cool thing is that the checksum (rightmost 5) is the only single digit number that can satisfy this rule. In other words, if you know the first
#9 digit, you can calculate the checksum (last digit). In this problem, you will be calculte the checksum of an ISBN number.
#########
'''
'''
Helper function 1: check_legit_ISBN
Input: a list with 10 single digit number in it
Output: return "Legit" if the 10 digits form a legit ISBN number
        return "Not Legit" otherwise

Sample: [0,2,0,1,3,1,4,5,2,5] should return "Legit"
        [0,2,0,1,3,1,4,5,2,3] should return "Not Legit"

'''


def check_legit_ISBN(ISBNLis):
    q = 0
    n = 0
    for i in range(10, 0, -1):
        q = i * ISBNLis[i]
        n = n + q
    if n % 11 == 0:
        return "legit"
    else:
        return "not legit"


'''
Helper func 2: format output
input: a list with 10 numbers in it
output: format it to the correct ISBN format and return it
Sample:
[0,2,0,1,3,1,4,5,2,5] will become: "ISBN 020131452-5"
'''


def format_ISBN(ISBNLis):
    ISBNStr = "ISBN "
    for i in range(len(ISBNLis)):
        ISBNStr = ISBNStr + str(ISBNLis[i])
    ISBNStr = ISBNStr[:14] + "-" + ISBNStr[14:]
    return ISBNStr


'''
Helper func 3: checksum_ISBN
Input: a list with 9 single digit number in it (first 9 digit in ISBN)
Output: print out: "The correct checksum digit is:__. Now we have a legit ISBN: _____"
Hint: just loop through 0,1,2...X (X represents 10), test every one with helper func1 to find out the one checksum that forms a legit ISBN
with the correct ISBN in lis (10 numbers), call helper func2 to format it correctly. Then print the final result.
(Technical googling practice - google how to append or remove an element from a list)
'''


def checksum_ISBN(partISBN):
    newISBN = ""
    for i in range(len(partISBN)):
        partISBN.append(i)
        strcheck = check_legit_ISBN(partISBN)
        if strcheck == "legit":
            print("The correct checksum digit is: " + str(i))
            print("Now we have a legit " + (format_ISBN(partISBN)))
            return
        elif strcheck == "not legit":
            partISBN.pop()


'''
Main Func: Generate a ISBN by:
add 9 random nunmbers into a list
(Technical googling practice - how to generate random numbers?)
call helper func 3 to find the checksum

Repeat 10 times
Generate 10 good ISBN numbers with one function call (not 10 digits for 1 ISBN)
Sample:
The correct checksum digit is:8. Now we have a legit ISBN:123456789-8 
The correct checksum digit is:8. Now we have a legit ISBN:987654321-8 
etc.
'''


def generate_ten_ISBNs():
    for i in range(10):
        list = ['']
        for j in range(9):
            list.append(random.randint(0, 9))
        checksum_ISBN(list)


if __name__ == '__main__':
    print("****Question 1****")
    easy_hello_loop1_for(4)
    print("****Question 2****")
    smaller_value(8, 9)
    print("****Question 3****")
    my_len([1, 3, 1, 4, 5])
    print("****Question 4****")
    cate_letters(['rt', 'asdf', 'ton', 'er', 'user'])
    print("****Question 5****")
    two_strings1("banana", "apples")
    print("****Question 6****")
    two_strings2("helloworld", "2435232399")
    print("****Question 7****")
    love6(6, 4)
    love6(4, 5)
    love6(1, 5)
    print("****Question 8****")
    generate_ten_ISBNs()
    # you can add your functions calls here
    # Please keep all the function calls and result printing
