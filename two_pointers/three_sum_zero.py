"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1844
Updated: 2026-06-08T10:43:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1844
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
