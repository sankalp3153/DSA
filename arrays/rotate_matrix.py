"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1176
Updated: 2025-11-26T17:21:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1176
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
