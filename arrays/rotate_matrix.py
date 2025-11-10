"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1130
Updated: 2025-11-10T20:30:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1130
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
