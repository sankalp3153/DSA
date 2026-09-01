"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 2142
Updated: 2026-09-01T21:13:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2142
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
