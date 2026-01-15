"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1360
Updated: 2026-01-15T19:18:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1360
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
