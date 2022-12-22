"""Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only."""

s1 = "Hello World"
s2 = "   fly me   to   the moon  "


#with split function and space complexity O(n)
def lengthOfLastWord1(s):
    lst = s.split() #initilising a list of words by spliting the sentence using split function
    if len(lst)==0: #if there is now word then return 0
        return 0
    else:
        return len(lst[-1]) #else return length of last word


#space complexity O(0)
def lengthOfLastWord2(s):
        i,length = len(s)-1,0 #initialising the variables

        while s[i] ==" ": #using loop to find if there is any trailing spaces in the sentence
            i -= 1 #decrementing the variable
        while i>=0 and s[i] != " ": #after the first loop ends that means it found a word then looping until the end of the sentence or until it found a space
            length += 1 #incrementing length with every word found
            i -= 1 #decrementing the variable
        return length #returning length of the last word

solution1 = lengthOfLastWord1(s1)
solution2 = lengthOfLastWord2(s2)

print(solution1)
print(solution2)