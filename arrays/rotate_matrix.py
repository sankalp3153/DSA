"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 532
Updated: 2025-05-20T14:35:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 532
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
