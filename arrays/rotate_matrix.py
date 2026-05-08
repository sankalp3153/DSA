"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1751
Updated: 2026-05-08T20:40:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1751
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
