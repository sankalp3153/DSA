"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1337
Updated: 2026-01-07T17:31:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1337
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
