"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 854
Updated: 2025-08-18T10:48:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 854
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
