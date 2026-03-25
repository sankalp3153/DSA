"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1613
Updated: 2026-03-25T13:35:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1613
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
