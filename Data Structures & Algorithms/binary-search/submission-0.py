class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #First we will have to set boundries
        #That means set left and right
        l, r = 0, len(nums) - 1
        #Now we will half the size based on is our
        #target greter or lesser than mid point
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1
        