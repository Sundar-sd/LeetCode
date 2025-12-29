class solution:
    def TwoSum(self,nums:list[int] , target : int ):
        seen = {}
        for index , value in enumerate(nums):
            needed = target - value

            if needed in seen:
                return seen[needed],[index]

            seen[value]=[index]

nums = [7,4,35,6,3]
target = 9
sol = solution()
result = sol.TwoSum(nums, target)
print("Indices:", result)