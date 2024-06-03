#Python exercise questions
#Help you getting familiar with Python syntax

#Grading:

#IMPORTANT NOTICE:
#A good practice in coding is to show your customer a working version and tell them
#what new features you want to add next.
#Thus, we require you to submit all your homework as a working version. If you
#only know how to solve 7/10 questions, just submit the 7 that runs without errors.
#For incomplete answers, comment the code out and print a line tell us your progress
#E.g. "Problem 3 is a completed but has run time errors"
#or "problem 5 is incomplete, but I did 75% of the work."

#Complete HW + correct results: 10pt
#Each question has a equal share of the total points
#Code that does not run will have only 2pt.
#No submission: 0%

#Please follow the required input/output and function names
#Main function is at the end of the file
#Please call all of your completed functions and print the results out

#Please define all the needed input variables in your main function directly and not asking for
#user input. Also, please format the output from each function and print them out in the main.

'''
 1. Input: Count
 Output: print Count number of "hello":
            1th hello
           2th hello...
 IMPORTANT: copy to visualizer, observe the behavior
'''

def easy_hello_loop1_for(Count):
    for x in range(Count):
        print("{}th hello".format(x+1))


'''
2.Input: number x,y
 Output: return the smaller value of the two
 Do it by yourself, no system calls like min()
'''
def smaller_value(x,y):
    if x>y:
        return y
    else:
        return x

'''
3. Do not use len(). Write a function to calculate how many elements do you have in your list, and return it
'''
def my_len(lis):
    count = 0
    for x in lis:
        count += 1
    return count

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
    #declare list
    Letter2 = []
    Letter3 = []
    Letter4 = []
    #for loop iterate thru list
    #if condition to categorize and sort into lists of 2 to 4 letter len
    for x in LongStr:
        if len(x)==2:
            Letter2.append(x)
        if len(x)==3:
            Letter3.append(x)
        if len(x)==4:
            Letter4.append(x)
    return Letter2, Letter3, Letter4


'''
5. input: a string with letters in it, a string with numbers in it.
We assume they have same amount of characters/length. 
output: go through the two strings together, print out elements by index
format "the elements at index __ from string1 is __, from string2 is ___"
'''
def two_strings1(str1,str2):
    for i in range(len(str1)):
        print(" Elements at index {} in string1: '{}'. and in string2: '{}'".format(i, str1[i], str2[i]))


'''
6. input: a string with letters in it, a string with numbers in it
output: go through the two strings together. At index i, if the number in str2 is even, put the letter in str1 into evenStr
if the number is odd, put the letter into oddStr. Return the even/odd strings
Sample: "helloworld" "2435232399"
gives evenStr="heoo" oddStr="llwrld"
'''
def two_strings2(str1,str2):
    evenStr, oddStr = ('', )*2
    for i in range(len(str1)):
        if int(str1[i]) % 2 == 0:
            evenStr += str2[i]
        else:
            oddStr += str2[i]
    return evenStr, oddStr
'''
7.
The number 6 is a truly great number. Given two int values, a and b, return True
if either one is 6. Or if their sum or difference is 6.
Note: the function abs(num) computes the absolute value of a number.

love6(6, 4) returns True
love6(4, 5) returns False
love6(1, 5) returns True
'''
def love6(a,b):
    if a or b == 6:
        return True
    if a+b == 6 or abs(a-b) == 6:
        return True
    else: return False

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
    pos = 10
    sum = 0
    for i in range(len(ISBNLis)):
        sum += ISBNLis[i] * pos
        pos -= 1
    if sum % 11 == 0:
        return "Legit"
    else:
        return "Not Legit"
'''
Helper func 2: format output
input: a list with 10 numbers in it
output: format it to the correct ISBN format and return it
Sample:
[0,2,0,1,3,1,4,5,2,5] will become: "ISBN 020131452-5"
'''
def format_ISBN(ISBNLis):
    stringISBN = "ISBN "
    for i in range(len(ISBNLis)-1):
        stringISBN += str(ISBNLis[i])
    stringISBN += '-'
    stringISBN += str(ISBNLis[9])
    return stringISBN

'''
Helper func 3: checksum_ISBN
Input: a list with 9 single digit number in it (first 9 digit in ISBN)
Output: print out: "The correct checksum digit is:__. Now we have a legit ISBN: _____"
Hint: just loop through 0,1,2...X (X represents 10), test every one with helper func1 to find out the one checksum that forms a legit ISBN
with the correct ISBN in lis (10 numbers), call helper func2 to format it correctly. Then print the final result.
(Technical googling practice - google how to append or remove an element from a list)
'''
def checksum_ISBN(partISBN):

    for x in range(0, 10):
        partISBN.append(x)
        if check_legit_ISBN(partISBN) == "Legit":
            print("The correct checksum digit is {}. The legitimate ISBN: {}".format(x, format_ISBN(partISBN)))
            return
        elif check_legit_ISBN(partISBN) == "Not Legit":
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
    import random
    a=1
    while a<11:
        rand_list = []

        for b in range (9):
            rand_list.append(random.randrange(0,9))
        print("{}.".format(a), end='')
        checksum_ISBN(rand_list)
        a += 1

if __name__ == '__main__':
    #variables
    num_list = [1,2,3,4,5,6,7,1]
    string_list = ['jeff', 'caro', 'home', 'nap', 'cook', 'poo', 'hi', 'no', 'bite']
    letter2, letter3, letter4 = ([], )*3
    legitISBN = [0, 2, 0, 1, 3, 1, 4, 5, 2, 5]
    badISBN = [0, 2, 0, 1, 3, 1, 4, 5, 2, 0]
    nineISBN = [0, 2, 0, 1, 3, 1, 4, 5, 2]
    #isbnEndinone= [0,7,8,6,0,1,6,5,3] for my troubleshooting purpose, ignore please


    print("****Question 1****")
    #you can add your functions calls here
    #Please keep all the function calls and result printing
    easy_hello_loop1_for(4)

    print("****Question 2****")
    print("The smaller value of 10 and 5 is:", smaller_value(10,5))

    print("****Question 3****")
    print("The list is:", num_list)
    print("The number of elements in test_list is:", my_len(num_list))

    print("****Question 4****")
    ##im unsure of output format that is required
    ##so i outputted the function result twice in two different ways
    print("The list is", string_list)
    print("Sorted lists", cate_letters(string_list))
    letter2, letter3, letter4 = cate_letters(string_list)
    print("2 Letters:", letter2)
    print("3 Letters:", letter3)
    print("4 Letters:", letter4)

    print("****Question 5****")
    two_strings1("ABCD", "1234")

    print("****Question 6****")
    print("The strings are '123456' and 'oeOEoe'")
    print(two_strings2("123456", "oeOEoe"))
    str_even, str_odd = two_strings2("123456", "oeOEoe")
    print("Even String= '{}', Odd String='{}".format(str_even, str_odd))

    print("****Question 7****")
    print("1,5", love6(1, 5))
    print("11,5", love6(11, 5))
    print("0,3", love6(0, 3))
    print("6,0", love6(6, 0))

    print("****Question 8****")
    #legitISBN = [0, 2, 0, 1, 3, 1, 4, 5, 2, 5]
    #badISBN = [0, 2, 0, 1, 3, 1, 4, 5, 2, 0]
    #nineISBN = [0, 2, 0, 1, 3, 1, 4, 5, 2]
    print("*~ Check helper function: check_legit_ISBN ~*")
    print((legitISBN),check_legit_ISBN(legitISBN))
    print(badISBN,check_legit_ISBN(badISBN))
    print("*~ Check helper function: format_ISBN ~*")
    print(format_ISBN(legitISBN))
    print("*~ Checking helper function checksum ~*")
    checksum_ISBN(nineISBN)
    #checksum_ISBN(isbnEndinone) for my troubleshooting purposes, please ignore
    print("***~ Checking main function  ~****")
    generate_ten_ISBNs()




