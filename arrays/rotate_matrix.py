"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1636
Updated: 2026-04-02T18:22:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1636
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
