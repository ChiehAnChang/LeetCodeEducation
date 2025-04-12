from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Let's initial the three important sets.
        row_set = set()
        col_set = set()
        sub_Sudoku_set = set()
        
        # Check the row by row first
        for i in range(9):
            for j in range(9):
                # Check if the current cell is not empty
                if board[i][j] != '.':
                    # Check if the number already exists in the row set
                    if board[i][j] in row_set:
                        return False
                    else:
                        row_set.add(board[i][j])
        
        # Check the column by column
        for j in range(9):
            for i in range(9):
                # Check if the current cell is not empty
                if board[i][j] != '.':
                    # Check if the number already exists in the column set
                    if board[i][j] in col_set:
                        return False
                    else:
                        col_set.add(board[i][j])
                        
        # Check the sub-Sudoku by sub-Sudoku
        
        row_index = 0
        col_index = 0
        
        while row_index < 3:
            
            while col_index < 3:
                
                for i in range(row_index * 3, row_index * 3 + 3):
                    for j in range(col_index * 3, col_index * 3 + 3):
                        # Check if the current cell is not empty
                        if board[i][j] != '.':
                            # Check if the number already exists in the sub-Sudoku set
                            if board[i][j] in sub_Sudoku_set:
                                return False
                            else:
                                sub_Sudoku_set.add(board[i][j])
                col_index += 1
                sub_Sudoku_set.clear()
                
            col_index = 0
            row_index += 1
            
                