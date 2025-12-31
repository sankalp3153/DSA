"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1314
Updated: 2025-12-31T11:58:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1314
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
