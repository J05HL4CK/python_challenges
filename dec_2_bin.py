def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary += str(decimal%2)
        decimal = decimal // 2
    
    res = binary[::-1]
    return res

decimal_to_binary(0)