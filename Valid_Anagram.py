# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        dict1 = {}
        for i in s :
            if i in dict.keys():
                dict[i] += 1
            else :
                dict[i] = 1
        for j in t :
            if j in dict1.keys():
                dict1[j] += 1
            else :
                dict1[j] = 1

        else :
            if dict == dict1 :
                return True
            else :
                return False

s = "rat"
t = "car"
a = Solution()
s = "anagram"
t = "nagaram"
print(a.isAnagram(s,t))





