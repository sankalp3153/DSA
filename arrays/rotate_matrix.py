"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 969
Updated: 2025-09-19T10:29:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 969
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
