"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 900
Updated: 2025-08-29T15:51:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 900
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
