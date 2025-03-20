"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 325
Updated: 2025-03-20T21:29:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 325
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
