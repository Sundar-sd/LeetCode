from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum =0
        for i in accounts:
            current_sum = 0
            for j in i:
                current_sum +=j

                if current_sum > max_sum:
                    max_sum = current_sum
        return max_sum


accounts = [[1,2,3],[3,2,1]]
sol = Solution()
result = sol.maximumWealth(accounts)
print(result)