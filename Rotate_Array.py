# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         for i in range(k):
#             last_element = nums[len(nums)-1]
#             for j in range(len(nums)-1,0,-1):
#                 nums[j] = nums[j-1]
#             nums[0] = last_element
#         print(nums)
class Solution:
    def reverse (self, nums, i, j) :
        li = i
        ri = j

        while li < ri:
            temp = nums[li]
            nums[li] = nums[ri]
            nums[ri] = temp

            li += 1
            ri -= 1
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k < 0 :
            k += len(nums)

        self.reverse(nums, 0, len(nums) - k - 1);
        self.reverse(nums, len(nums) - k, len(nums) - 1);
        self.reverse(nums, 0, len(nums) - 1);
# có nghĩa là chỉ cần thiết lập max cho 7 lần nếu sau 7 lần quy luật lặp lại như cũ ( bằng phép chia lấy dư cho 7)
nums = [1,2,3,4,5,6,7]
k = 3
s = Solution()
s.rotate(nums,k)

