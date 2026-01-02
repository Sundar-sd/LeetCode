from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_sum = 0
        max_sum =0

        for i in gain :
            current_sum += i

            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum


gain = [-5,1,5,0,-7]
sol = Solution()
result = sol.largestAltitude(gain)
print(result)