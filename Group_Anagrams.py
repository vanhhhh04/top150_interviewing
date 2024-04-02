# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
# class Solution(object):
#     def groupAnagrams(self, strs):

#         freq = {}

#         for word in strs:

#             newWord = ''.join(sorted(word))

#             if newWord not in freq:
#                 freq[newWord] = []

#             freq[newWord].append(word)

#         return freq.values()




# strs = ["eat","tea","tan","ate","nat","bat"]

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for i in strs :
            newword = "".join(sorted(i))
            if newword in dict.keys():
                dict[newword].append(i)
            else :
                dict[newword] = []
                dict[newword].append(i)

        return dict.values()
strs = ["eat","tea","tan","ate","nat","bat"]
# newword = "".split(sorted(strs[0]))
s = Solution()
print(s.groupAnagrams(strs))


























# a = Solution()
# strs = ["eat","tea","tan","ate","nat","bat"]
# print(a.groupAnagrams(strs))

