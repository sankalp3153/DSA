"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1935
Updated: 2026-07-06T18:18:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1935
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
