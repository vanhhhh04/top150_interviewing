# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise

# Input:
nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
greatest_step = nums[0]
def max_step(index,value):
    max = 0
    for i in range(index+1,index+value+1):
        if nums[i] > max :
            max = nums[i]
    return i,max
for i in range(0,len(nums)):
    greatest_step += max_step(i,nums[i])


