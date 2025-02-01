"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 141
Updated: 2025-02-01T22:29:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 141
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
