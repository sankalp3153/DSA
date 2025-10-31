"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1107
Updated: 2025-10-31T21:55:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1107
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
