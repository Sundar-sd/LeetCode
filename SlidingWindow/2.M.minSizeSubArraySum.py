class Solution:
    def minSubArraySum(self , nums:list[int] , target : int):

        left = 0
        current_sum = 0
        min_len = float('inf')

        for right in range (len(nums)):
            current_sum+= nums[right]

            while current_sum >= target:
                min_len = min(min_len , right - left +1)
                current_sum-=nums[left]
                left +=1

        return 0 if min_len == float('inf') else min_len

nums = [2,3,1,2,4,3]
target = 7
sol = Solution()
r = sol.minSubArraySum(nums,target)
print(r)