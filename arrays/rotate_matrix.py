"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 2326
Updated: 2026-11-03T21:45:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2326
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
