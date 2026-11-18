"""
In-place 90-degree clockwise N x N matrix rotation via transpose + row reversal.
Time: O(n^2) | Space: O(1)
"""

from typing import List


def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    for row in matrix:
        row.reverse()
    return matrix
