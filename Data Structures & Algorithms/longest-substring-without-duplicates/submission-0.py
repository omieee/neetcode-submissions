class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        l = 0
        r = 0
        maximum = 0

        while r < len(s):
            char = s[r]
            if char in substring:
                substring.remove(s[l])
                l += 1
            else:
                substring.add(char)
                r += 1
                maximum = max(len(substring), maximum)
                
        return maximum

        