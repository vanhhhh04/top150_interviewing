# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.
# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9


# class Solution:
#     def longestConsecutive(self, nums):
#         longest = 0
#         set_num = set(nums)

#         for i in nums :
#             if (i-1) not in set_num :
#                 length = 1
#                 while i+length in set_num:
#                     length += 1
#                 longest = max(longest,length)
#         return longest

class Solution:
    def longestConsecutive(self, nums):
        longest = 0
        set_num = set(nums)
        for i in set_num :
            if i-1 not in set_num :
                length = 1
                while i+length in set_num :
                    length += 1
                longest = max(length,longest)
        return longest

nums = [0,3,2,1,4,76,45,7,8,9]
set_num = {0, 1, 2, 3, 4, 7, 8, 9, 76, 45}
print(set_num)
s = Solution()
print(s.longestConsecutive(nums))


