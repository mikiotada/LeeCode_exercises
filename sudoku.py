""""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

"""

import numpy as np
from collections import defaultdict
class Solution:
    """
    O(n^2)

    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board = np.array(board)

        for row in range(9):
            if self.is_duplicate(board[row]):
                return False
            for col in range(9):
                if self.is_duplicate(board[:, col]):
                    return False

                if (col in [0, 3, 6]) and (row in [0, 3, 6]):
                    if self.is_duplicate(board[row:row+3, col:col+3]):
                        return False

        return True

    def is_duplicate(self, nes_lis):
        d = defaultdict(int)
        for lis in nes_lis:
            for num in lis:
                if num != '.':
                    d[num] += 1

                    if d[num] == 2:
                        return True

        return False
