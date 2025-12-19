class Solution:
    def containsDuplicate(self ,nums: list[int] ):
       
        set_n = set(nums)
        if len(nums) != len(set_n):
            return True
        return 

nums=[1,2,3,3]
sol = Solution()
result = sol.containsDuplicate(nums)
print(result)
