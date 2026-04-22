"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1705
Updated: 2026-04-22T23:10:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1705
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
