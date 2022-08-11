# def mumbles(string):
#     """Return a string, each character multiplied by its index."""


string = "abcd"

# for letter in string.split():
#     result = ""
#     for letter, value in enumerate()

def mumbles(string):
    """Return a string of characters multiplied by the index position."""
    index = 1
    result = []
    for letter in list(string):
        value = letter * index
        index += 1
        result.append(value.title())
    print("-".join(result))
mumbles(string)

