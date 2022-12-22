"""Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
..."""

columnNumber = 28

def convertToTitle(columnNumber):
        Alpha = [chr(x) for x in range(ord('A'), ord('Z')+1)] #make a list of characters form a to z in capital using ord which gives us integer value of a character
        result = []
        while columnNumber > 0: #iterating until num is not zero
            result.append(Alpha[(columnNumber-1)%26]) #appending the char in empty list by accessing it by their index value using mod operator and also substracting 1 form num because index start from zero in our char list 
            columnNumber = (columnNumber-1)//26 #updating num value 
        result.reverse() #reversing the list to get the right order
        return ''.join(result) #join the string

sol = convertToTitle(columnNumber)
print(sol)