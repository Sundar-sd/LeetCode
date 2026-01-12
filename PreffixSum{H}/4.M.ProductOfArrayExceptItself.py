from typing import List
class Solution:
    def ex(self , nums:List[int]):

        n = len(nums)
        ans = [1]*n

        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        sufix = 1
        for i in range(n-1 , -1 ,-1):
            ans[i] *= sufix
            sufix *= nums[i]
        
        
        return ans 
sol = Solution()
print(sol.ex([1,2,3,4]))