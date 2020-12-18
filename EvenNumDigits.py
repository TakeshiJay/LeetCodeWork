```
  This function finds the amount of numbers within a list and returns the amount of numbers that have a even length
```
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                x+=1
        return(x)
