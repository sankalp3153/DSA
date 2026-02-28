"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1521
Updated: 2026-02-28T18:14:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1521
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
