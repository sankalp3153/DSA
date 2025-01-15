"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 72
Updated: 2025-01-15T13:55:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 72
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
