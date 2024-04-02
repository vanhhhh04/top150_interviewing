# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         tmp = []
#         n = len(nums)/2
#         for i in nums:
#             if i not in tmp :
#                 tmp.append(i)

#         dict = {}
#         for i in tmp :
#             dict[i] = 0
#         for i in dict.keys():
#             for j in range(0,len(nums)):
#                 if (i == nums[j]):
#                     dict[i] += 1
#         for i,j in dict.items() :
#             if j > n :
#                 return i
class Solution:
    def majorityElement(self, nums) -> int:
        n = len(nums)
        count_map = {}

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            if count_map[num] > n / 2:
                return num

        return -1

nums = [2,2,1,1,1,2,2]

s = Solution()
print(s.majorityElement(nums))