"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise."""

s = "A man, a plan, a canal: Panama"

#function using two pointers
def isPalindrome(s):
        l =0 #initialising the variable
        r = len(s)-1 #initialising the variable
        while l<r: #iterating until l != r
            if not s[l].isalnum(): #if char is not alphanumeric then increment the l variable 
                l += 1
            elif not s[r].isalnum(): #if char is not alphanumeric then decrement the r variable 
                r-=1
            else:
                if s[l].lower()!=s[r].lower(): #check if l an r are both equal by converting them in lower case if not then return false 
                    return False    
                else: #updating the variables
                    l += 1
                    r-= 1
        return True #return true if string is palindrome

sol = isPalindrome(s)
print(sol)