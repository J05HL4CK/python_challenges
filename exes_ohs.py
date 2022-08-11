# Check to see if a string has the same amount of 'x's and 'o's.
# The method must return a boolean and be case insensitive.
# The string can contain any char.
import re
def xoxo(string):
    """return boolean if string has the same amount of 'x's and 'o's."""
    exes = 0
    ohs = 0
    split_string = list(string)
    for char in split_string:
        if char == 'x':
            exes += 1
        if char == 'o':
            ohs += 1
        elif char != 'x' and char != 'o':
            print(True)
            break
    if exes == ohs:
        print(True)
    else:
        print(False)

string1 = "ooojskfh"
string2 = "xoxoxoxo"
string3 = "xxxooo"
string4 = "oxoxox"
string5 = "XOxxOO"
xoxo(string1)
xoxo(string2)
xoxo(string3)
xoxo(string4)
xoxo(string5)

