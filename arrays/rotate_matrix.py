"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1475
Updated: 2026-02-16T16:15:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1475
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
