"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1291
Updated: 2025-12-26T20:29:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1291
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
