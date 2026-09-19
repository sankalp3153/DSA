"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 2188
Updated: 2026-09-19T12:30:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2188
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
