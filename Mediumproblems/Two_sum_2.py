class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        left = 0
        right = len(numbers)-1

        while left < right:
            current_sum = numbers[left]+numbers[right]

            if current_sum == target:
                return [left + 1 , right + 1]
           
            elif current_sum > target:
                right-=1
            else:
                left+=1
            

numbers = [1,2,3,4]
target = 6
sol = Solution()
result = sol.twoSum(numbers,target)
print(result)