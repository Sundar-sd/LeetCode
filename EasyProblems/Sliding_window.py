class Solution:
    def findMaxAverage(self, nums: list[int], k: int):
        cur = sum(nums[:k])
        max = cur

        for i in range(k,len(nums)):
            cur += nums[i] - nums[i - k]

            if cur > max :
                max = cur
        return max/k

nums = [5, 3, 2, 6, 1, 4]
k = 3
sol = Solution()
result = sol.findMaxAverage(nums,k)
print(result)