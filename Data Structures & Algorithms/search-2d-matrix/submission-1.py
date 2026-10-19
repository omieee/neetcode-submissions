class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #First we will have to set boundries
        #That means set left and right
        for nums in matrix:
            l, r = 0, len(nums) - 1
            #Now we will half the size based on is our
            #target greter or lesser than mid point
            while l <= r:
                mid = (l + r) // 2 # Finding the mid and round down
                if target > nums[mid]: #Should i look right
                    l = mid + 1
                elif target < nums[mid]: #Should i look left
                    r = mid - 1
                else:
                    return True #Bingo
        return False
        