"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 2211
Updated: 2026-09-29T10:37:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2211
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
