from typing import List
class Solution:
    def paei(self  , nums:List[int]):

        ans = [1]*len(nums)

        sufix = 1
        for j in range(len(nums)-1,-1,-1):
            ans[j] *= sufix
            sufix *= nums[j]

        return ans
sol = Solution()
print(sol.paei([1,2,3,4]))

