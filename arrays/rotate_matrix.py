"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1429
Updated: 2026-02-04T19:37:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1429
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
