# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
class Solution(object):
    def wordPattern(self, pattern, s):
        dic={}
        dic2={}
        s=s.split(' ')
        if len(s)!=len(pattern):
            return(False)
        for i,j in zip(pattern,s):
            if i in dic:
                if dic[i]!=j:
                    return(False)
            else:
                dic[i]=j
            if j in dic2:
                if dic2[j]!=i:
                    return(False)
            else:
                dic2[j]=i
        return(True)
a = Solution()
pattern = "abba"
s = "dog cat cat dog"
a.wordPattern(pattern,s)

