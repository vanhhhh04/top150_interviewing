class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        dem = 0
        tg = []
        for i in nums :
            if i != val :
                dem += 1
                tg.append(i)
        nums[:] = tg[:]
        return tg
s = Solution()
a = [1,4,5,2,3,4,2]
print(s.removeElement(a,4))
