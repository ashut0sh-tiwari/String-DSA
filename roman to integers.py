"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer."""

s = "III"

def romanToInt(s): #function to change roman into integer
    #dictionary to store data in key value pair
        rti={
            "I":1,
            "V":5,
            "X":10,
            "L":50,

            "C":100,
            "D":500,
            "M":1000
        } 
        N = len(s) #initialising the variable
        num = 0 #initialising the variable
        i = N-1 #initialising the variable
        while i >=0: #looping until last element
            if i<N-1 and rti[s[i]]<rti[s[i+1]]: #checking if number is smaller than preceding number because in roman integers numbers usually are written in left to right in decreasing order except in case of 4 or 9
                num -= rti[s[i]] #if number is smaller than its next number then subtract that number value from the num
            else:
                num+=rti[s[i]] #if number is greater than its next number then add that number value from the num
            i-=1 #incrementing the index
        return num #returning the sum of roman number in integer form

solution = romanToInt(s)
print(solution)
