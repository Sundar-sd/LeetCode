from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        freq = {0:1}
        prefix_sum = 0

        for num in nums:
            prefix_sum+= num

            if prefix_sum - k in freq:
                count+=freq[prefix_sum - k]

            if prefix_sum in freq:
                freq[prefix_sum]+=1
            else:
                freq[prefix_sum] = 1

        return count

nums = [-1,1,-2,2,3]
k = 3 
sol = Solution()
r = sol.subarraySum(nums,k)
print (r)