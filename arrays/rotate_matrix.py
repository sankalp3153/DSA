"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1866
Updated: 2026-06-12T14:57:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1866
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
