"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1498
Updated: 2026-02-23T15:29:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1498
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
