"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).
"""




from collections import defaultdict
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        O(n^2)
        """
        d = defaultdict(int)
        size = len(matrix)
        for row in range(size):
            for col in range(size):
                d[tuple([row, col])] = matrix[row][col]

        for row in range(size):
            for i in list(range(0, size)):
                matrix[i][size-row-1] = d[(row, i)]
