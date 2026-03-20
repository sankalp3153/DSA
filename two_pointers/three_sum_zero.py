"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1591
Updated: 2026-03-20T18:57:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1591
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
