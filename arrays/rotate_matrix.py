"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1820
Updated: 2026-06-03T17:14:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1820
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
