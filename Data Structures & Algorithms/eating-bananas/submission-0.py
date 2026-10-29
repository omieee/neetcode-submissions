class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r # To start with this will be a deffinit answer

        #will start our binary search
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h: # either we have finised eating earlier or just in time, we will see if we can eat any slower and still finish all
                res = min(res, k) # will save the min of previous slowest and k speed
                r = k -1 # that means no other possiblity toward sight will be slower
            else:
                # we need to eat faster
                l = k + 1
        return res

        