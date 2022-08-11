# take numberin base 10
# divide the number by the floor  //2 record result
# take the modulus of the number divided 2 record result
# take the floor result and repeat until 0 
# take the modulo results and j
# 
binary_number = []
def dec_to_bin(number):
    if number > 0:
        dec_to_bin(number // 2)
        binary_number.append(number % 2)
    binary = "".join(map(str,binary_number))
    return binary
# number = int(input("Enter an integer: " ))
# dec_to_bin(number)

# # print(*binary_number, sep = "")
print(binary)