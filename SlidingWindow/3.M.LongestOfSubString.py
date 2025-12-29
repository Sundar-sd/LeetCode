class Solution:
    def lengthOfLongestSubstring(self , s: str):
        char_set = set()
        left = 0
        max_sum = 0

        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[left])
                left+=1

            char_set.add(s[i])
            max_sum = max(max_sum ,i - left + 1 )

        return max_sum
s = "abcabcbb"
sol = Solution()        
result = sol.lengthOfLongestSubstring(s)
print(result)