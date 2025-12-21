class Solution:
    def maxSubArray(self , nums):
        current_sum = nums[0]
        best_sum = nums[0]


        for i in range(1,len(nums)):
            if current_sum < 0:
                current_sum = nums[i]
            else:
                current_sum+=nums[i]

            if current_sum > best_sum:
                best_sum = current_sum

        return best_sum



nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
result = sol.maxSubArray(nums)
print(result)