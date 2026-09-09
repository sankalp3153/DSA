"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 2165
Updated: 2026-09-09T13:07:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2165
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
