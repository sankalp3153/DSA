"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1015
Updated: 2025-09-30T20:08:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1015
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
