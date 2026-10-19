class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Which row has the solution
        ROWS, COLS = len(matrix), len(matrix[0])

        TOP_ROW, BOT_ROW = 0, ROWS - 1

        while TOP_ROW <= BOT_ROW:
            MID_ROW = (TOP_ROW + BOT_ROW) // 2
            if target > matrix[MID_ROW][-1]:
                TOP_ROW = MID_ROW + 1
            elif target < matrix[MID_ROW][0]:
                BOT_ROW = MID_ROW - 1
            else:
                break
        if not(TOP_ROW <= BOT_ROW):
            return False
        
        MID_ROW = (TOP_ROW + BOT_ROW) // 2

        l, r = 0, len(matrix[MID_ROW]) - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[MID_ROW][m]:
                l = m + 1
            elif target < matrix[MID_ROW][m]:
                r = m - 1
            else:
                return True
        return False


        