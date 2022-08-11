import re

def XO(string):
    """Returns a boolean if the string contains the same number of x or os"""
    ex = 0
    oh = 0
    o_x = re.findall("[ox]", string.lower())
    y = re.findall("[^ox]", string.lower(),)
    for i in o_x:
        if i == "x":
            ex += 1
        if i == "o":
            oh += 1
    if ex == oh:
        print(True)
    elif len(list(string)) == len(y):
        print(True)
    else:
        print(False)




