"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1728
Updated: 2026-04-30T14:28:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1728
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
