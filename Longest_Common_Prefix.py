# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings
def longest_common(strs):
    start = strs[0]
    for i in strs[1:]:
        while i.find(start) != 0:
            start = start[:-1]
            if not start :
                return ""
    return start
strs = ["flower","flow","hello"]
print(longest_common(strs))
# a = strs[1].find("flow")
# print(a)

