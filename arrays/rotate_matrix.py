"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 555
Updated: 2025-05-24T20:58:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 555
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
