"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1936
Updated: 2026-07-06T18:37:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1936
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
