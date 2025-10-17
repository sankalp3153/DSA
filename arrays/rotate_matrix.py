"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1061
Updated: 2025-10-17T10:36:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1061
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
