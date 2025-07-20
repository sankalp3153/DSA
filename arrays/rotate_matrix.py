"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 739
Updated: 2025-07-20T15:38:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 739
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
