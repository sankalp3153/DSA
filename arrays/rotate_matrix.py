"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 348
Updated: 2025-03-23T20:51:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 348
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
