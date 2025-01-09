"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 49
Updated: 2025-01-09T17:47:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 49
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
