"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 394
Updated: 2025-04-04T20:51:26+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 394
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
