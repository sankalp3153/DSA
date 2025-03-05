"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 256
Updated: 2025-03-05T10:06:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 256
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
