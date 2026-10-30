"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 2303
Updated: 2026-10-30T15:24:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2303
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
