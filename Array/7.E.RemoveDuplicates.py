from typing import List
class Solution:
    def removeduplicates(self , nums:List[int]):

        write = 1

        for i in range (1,len(nums)):
            if nums[i]!= nums[i-1]:
                nums[write] = nums[i]
                write+=1

        return write


nums =[1,1,7,7,8,9,9]
sol = Solution()
result = sol.removeduplicates(nums,)
print (result)
