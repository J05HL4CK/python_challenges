import re
list = [1,4,5,6,7,"a","b","c","d","e","f","g","h",9]
def filter(list):
    filt = re.findall("[0-9]", string)
    print(filt)

filter(list)