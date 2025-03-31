"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 371
Updated: 2025-03-31T14:15:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 371
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
