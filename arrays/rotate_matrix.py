"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1452
Updated: 2026-02-08T20:02:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1452
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
