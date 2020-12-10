class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        holdInteger = 0
        nuList = []
        for i in nums:
            holdInteger += i
            nuList.append(holdInteger)
        return(nuList)
