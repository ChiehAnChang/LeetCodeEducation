from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row for duplicate numbers.
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        
        # Check each column for duplicate numbers.
        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        
        # Check each 3x3 sub-box for duplicate numbers.
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for i in range(box_row * 3, box_row * 3 + 3):
                    for j in range(box_col * 3, box_col * 3 + 3):
                        if board[i][j] != '.':
                            if board[i][j] in seen:
                                return False
                            seen.add(board[i][j])
        return True
