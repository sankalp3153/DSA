"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 417
Updated: 2025-04-14T15:22:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 417
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
