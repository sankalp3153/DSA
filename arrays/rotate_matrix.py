"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1153
Updated: 2025-11-21T22:54:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1153
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
