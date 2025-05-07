"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 486
Updated: 2025-05-07T15:36:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 486
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
