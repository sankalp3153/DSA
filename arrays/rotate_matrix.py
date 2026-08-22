"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 2096
Updated: 2026-08-22T18:34:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2096
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
