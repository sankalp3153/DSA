"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1406
Updated: 2026-01-30T14:55:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1406
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
