"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 578
Updated: 2025-06-03T10:39:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 578
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
