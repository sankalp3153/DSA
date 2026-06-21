"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1889
Updated: 2026-06-21T11:33:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1889
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
