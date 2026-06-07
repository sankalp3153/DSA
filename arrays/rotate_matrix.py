"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1843
Updated: 2026-06-07T21:17:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1843
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
