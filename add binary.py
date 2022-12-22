"""Given two binary strings a and b, return their sum as a binary string."""

a = "1010"
b = "1011"

def addBinary(a, b):
        output = int(a,2) + int(b,2) #first convert both binary into int and add them
        return "{:b}".format(output) #then return output number in binary form


#funtion to convert number into binary using recursion
# def DecimalToBinary(num):
     
#     if num >= 1:
#         DecimalToBinary(num // 2)
#     print(num % 2, end = '')

solution = addBinary(a,b)
print(solution)