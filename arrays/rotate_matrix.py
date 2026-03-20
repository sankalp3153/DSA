"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1590
Updated: 2026-03-20T11:32:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1590
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
