"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1199
Updated: 2025-12-01T17:49:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1199
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
