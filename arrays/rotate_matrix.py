"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 210
Updated: 2025-02-19T15:52:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 210
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
