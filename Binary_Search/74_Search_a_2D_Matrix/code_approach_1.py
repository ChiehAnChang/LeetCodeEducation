from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        # ── 1. Row selection ──
        top, bot = 0, m - 1
        while top <= bot:
            mid_row = (top + bot) // 2
            if matrix[mid_row][-1] < target:       # target is larger
                top = mid_row + 1
            elif matrix[mid_row][0] > target:      # target is smaller
                bot = mid_row - 1
            else:                                  # found candidate row
                break

        if top > bot:                              # no row fits
            return False
        row = (top + bot) // 2                     # candidate row index

        # ── 2. Column search ──
        left, right = 0, n - 1
        while left <= right:
            mid_col = (left + right) // 2
            val = matrix[row][mid_col]
            if val == target:
                return True
            elif val < target:
                left = mid_col + 1
            else:
                right = mid_col - 1

        return False
