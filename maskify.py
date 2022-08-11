# def maskify(credit_card):
#     """Returns a masked credit card number."""
#     tmp = str(credit_card[-4].rjust(len(credit_card), "#"))
#     print(tmp)

# maskify = lambda credit_card: credit_card[-4].rjust(len(credit_card), "#")

def mask(card):
    tmp = str(card)
    return tmp[-4:].rjust(len(tmp), "#")

