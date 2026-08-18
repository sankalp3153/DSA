"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 2073
Updated: 2026-08-18T14:05:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2073
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
