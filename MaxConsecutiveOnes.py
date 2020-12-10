class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count1 = 0
        count2 = 0
        for i in range(0,len(nums)):
            if nums[i] == 0:
                count1 = 0
            else:
                count1 += 1
                count2 = (max(count1,count2))
        return(count2)
