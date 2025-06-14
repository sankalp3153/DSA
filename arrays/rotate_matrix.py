"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 624
Updated: 2025-06-14T20:50:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 624
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
