"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 808
Updated: 2025-08-08T20:53:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 808
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
