class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sorted_s1 = "".join(sorted(s))
            sorted_t1 = "".join(sorted(t))
            if sorted_s1 == sorted_t1:
                return True
        return False   