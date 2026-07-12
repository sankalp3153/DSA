"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1958
Updated: 2026-07-12T23:41:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1958
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
