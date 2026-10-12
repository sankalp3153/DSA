"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 2257
Updated: 2026-10-12T12:10:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2257
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
