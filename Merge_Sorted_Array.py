# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result ca
class Solution(object):
    def merge(self,nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        print(id(nums1))
        tmp = 0
        result = []
        for i in range(m):
            result.append(nums1[i])
        for i in range(n):
            result.append(nums2[i])
        for i in range(m+n):
            for j in range(m+n-1):
                if result[j] > result[i]:
                    tmp = result[i]
                    result[i] = result[j]
                    result[j] = tmp

        nums1 = result


nums1 =[1,2,3,0,0,0]
m = 3
nums2 =[2,5,6]
n = 3
s = Solution()

s.merge(nums1, m, nums2, n)


