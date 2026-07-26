"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 2004
Updated: 2026-07-26T22:06:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2004
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
