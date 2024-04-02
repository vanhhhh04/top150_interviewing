# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
# def check_subsequence(s,t):
#     flag = 0
#     lst = []
#     for i in s :
#         a = t.find(i)
#         if a == -1 :
#             break
#         else :
#             lst.append(a)
#     flag = 1
#     for i in range(len(lst)-1) :
#         if lst[i+1] < lst[i] :
#             flag = 0
#             break
#     if len(lst) == len(s) and flag :
#         return True
#     return False

# s = "aaaaaa"
# t = "bbaaaa"
# print(check_subsequence(s,t))


a = "aaaaaa"
b = "bbaaaa"
s = Solution()
print(s.isSubsequence(a,b))