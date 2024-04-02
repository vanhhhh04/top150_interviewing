# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        tmp = []
        if intervals[0][1] < intervals[1][0]:
            tmp.append(intervals[0])
        for i in range(1,len(intervals)) :
            if intervals[i][0] <= intervals[i-1][1]:
                tmp.append([intervals[i-1][0],intervals[i][1]])
            else :
                tmp.append(intervals[i])
        return tmp
intervals = [[1,3],[2,6],[8,10],[15,18]]
s = Solution()
print(s.merge(intervals))