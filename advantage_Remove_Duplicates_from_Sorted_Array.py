# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
nums = [0, 1, 1, 2, 3]

# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         l = 0
#         dem = 0
#         tmp = {nums[0] : 1}
#         for i in range(0,len(nums)-1):
#             if (nums[i] == nums[i+1]):
#                 tmp[nums[i]] += 1
#             else :
#                 tmp[nums[i+1]] = 1
#         for i in tmp.keys():
#             if(tmp[i] == 1):
#                 nums[l] = i
#                 l += 1
#             if (tmp[i] >= 2) :
#                 nums[l] = i
#                 l += 1
#                 nums[l] = i
#                 l += 1
#         print(nums)
#         return l

# nums = [0,0,1,1,1,1,2,3,3]
# nums=[-1,0,0,0,0,3,3]
# s = Solution()
# s.removeDuplicates(nums)
class Solution(object):
    def removeDuplicates(self, nums):
        # Initialize an integer k that updates the kth index of the array...
        # only when the current element does not match either of the two previous indexes. ...
        k = 0
        # Traverse all elements through loop...
        for i in nums:
            # If the index does not match elements, count that element and update it...
            if k < 2 or i != nums[k - 2]:
                nums[k] = i
                k += 1
        return k
nums=[-1,0,0,0,0,3,3]
s = Solution()
print(s.removeDuplicates(nums))


