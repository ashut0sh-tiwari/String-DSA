"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""."""

strs = ["flower","flow","flight"]

def longestCommonPrefix(strs): #function to find the common prefix
        res = "" #creating a empty string variable
        for i in range(len(strs[0])): #looping in range of len of first string in the list
            for s in strs: #another loop to loop through the other string of the list at the same index
                if i == len(s) or s[i] != strs[0][i]: #if i is out of bounce or same character does not exist at the ith index of other string
                    return res #return res
            res += strs[0][i] #else adding that character to the res

        return res #return res

solution = longestCommonPrefix(strs)
print(solution)