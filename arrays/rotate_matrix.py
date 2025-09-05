"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 923
Updated: 2025-09-05T16:54:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 923
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
