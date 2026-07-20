class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lptr = 0
        rptr = len(s) - 1
        while lptr < rptr: # that is the mid point
            temp = s[lptr]
            s[lptr] = s[rptr]
            s[rptr] = temp
            lptr += 1
            rptr -= 1            
        