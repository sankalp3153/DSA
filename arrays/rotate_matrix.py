"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1383
Updated: 2026-01-25T15:05:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1383
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
