"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1567
Updated: 2026-03-14T18:44:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1567
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
