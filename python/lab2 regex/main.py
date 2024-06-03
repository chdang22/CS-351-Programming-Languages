# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



#for my reference, i was sick and have doctors appt so i missed group activities and need to look
#at this as i code to match expressions
#'^' -   start
#'$' -  till end
#[0-9]  any numbers in range 0-9
#[a-zA-Z] - letters
#\. - period
#\w -  word
#'+' - one or more characters
#'*' - zero or more characters
import re
#---Function: regex_match---
# Purpose: compares all strings looking for match using regex
#test pattern matches string, use int match to indicate match and print matches
#param: list of strings
#output: prints matches
def regex_match(string_list):
    #for loop compares all string in list
    for string in string_list:
        #if matched, mathced =1, if no match =0
        match = 0

        #if statements looking for match

        # integer
        if re.match("^[0-9]+$", string):
            pattern = "An integer."
            print("MATCH: {} matches the pattern: {} :)" .format(string, pattern))
            match = 1

        #float with 1+ digit after decimal
        if re.match("^[0-9]+\.[0-9]+$", string):
            pattern = " A float consists of 1 or more digits before and after decimal point."
            print("MATCH: {} matches the pattern: {} :)".format(string, pattern))
            match = 1

        #float with exactly 2 digits after the decimal point
        if re.match("^[0-9]+\.[0-9]{2}$", string):
            pattern = "A float with exactly 2 digits after the decimal point."
            print("MATCH: {} matches the pattern: {} :)".format(string, pattern))
            match = 1

        #float end with letter f (4.321f)
        if re.match("^[0-9]+\.[0-9]+f{1}$", string):
            pattern = "A float end with letter f (4.321f)"
            print("MATCH: {} matches the pattern: {} :)".format(string, pattern))
            match = 1

        #Capital letters, followed by small case letters, followed by digits
        if re.match("^[A-Z]+[a-z]+[0-9]+$", string):
            pattern = "Capital letters, followed by small case letters, followed by digits"
            print("MATCH: {} matches the pattern: {} :)".format(string, pattern))
            match = 1

        #Exactly 3 digits, followed by at least 2 letters
        if re.match("^[0-9]{3}[A-Za-z]{2,}$", string):
            pattern = "Exactly 3 digits, followed by at least 2 letters"
            print("MATCH: {} matches the pattern: {} :)".format(string, pattern))
            match = 1

        #no match
        if match == 0:
            print("{} doesn't match any pattern. :(" .format(string))

#---Function: remove_int_from_string---
#param: string
#goal: 1. find int at begin of string and remove it
#      2. find the begin index and end index of int
#      3. print found integer, index of integer and new string"
def remove_int_from_string(string):
    found_int = re.search("\d+", string)
    new_string = string.replace(found_int.group(0), '')
    intx = found_int.group(0)
    start=found_int.start()
    end = found_int.end()-1
    print("String:'{}.' Found integer {} at the beginning of this string starting at index {} and ending at index {} The rest of the string is '{}'".format(string, intx, start, end, new_string))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    int_string1 = "2023 spring"
    int_string2 = "91Days"
    str_list = ["22.11", "23", "66.71f", "123abcde", "sheep91",
                "Heart", "12.45", "66.7", "tiger134", "Valentines14"]
    regex_match(str_list)
    remove_int_from_string(int_string1)
    remove_int_from_string(int_string2)
