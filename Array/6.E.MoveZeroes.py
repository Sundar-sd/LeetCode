class Solution:
    def MoveZeroes(self,nums:[int]):

        a=0

        for i in range (len(nums)):
            if nums[i]!=0:
                nums[a],nums[i] = nums[i] , nums[a]
                a+=1

        return nums
nums = [0,1,0,8,91,0,0,1,5,0,6,4,9,8,1,0]
sol=Solution()
result=sol.MoveZeroes(nums)
print(result)