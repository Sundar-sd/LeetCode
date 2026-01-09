from typing import List
class Solution:
    def p(self , nums : List[int]):
        n = len(nums)
        res = [1]*n

        preffix = 1
        for i in range(n):
            res[i] = preffix
            preffix *= nums[i]


        suffix = 1
        for i in range(n-1 ,-1 ,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

nums = [1,2,3,4]
sol = Solution()
result = sol.p(nums)
print (result)