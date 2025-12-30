from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        h = {0:-1}
        current_sum = 0
        count = 0


        for i in range (len(nums)):
            if nums[i] == 0:
                current_sum -= 1
            else:
                current_sum += 1

            if current_sum in h:
                length = i - h[current_sum]
                count = max(length , count )
            else:
                h[current_sum] = i

        return count

