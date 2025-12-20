class Solution:
    def moveZeroes(self , nums=[int]):
        pos = 0

        for i in range(len(nums)):
            if nums[i]!=0:
                nums[pos] , nums[i] = nums[i] , nums[pos]
                pos +=1

        return nums
   
nums = [0,1,0,0,23,3]
sol = Solution()
result = sol.moveZeroes(nums)
print(result)