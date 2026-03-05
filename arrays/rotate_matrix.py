"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1544
Updated: 2026-03-05T13:34:40+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1544
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
