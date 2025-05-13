"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 509
Updated: 2025-05-13T12:37:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 509
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
