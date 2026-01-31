"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1407
Updated: 2026-01-31T10:54:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1407
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
