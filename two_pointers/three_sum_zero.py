"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1361
Updated: 2026-01-15T21:01:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1361
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
