"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 95
Updated: 2025-01-23T23:23:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 95
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
