"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 118
Updated: 2025-01-29T15:11:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 118
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
