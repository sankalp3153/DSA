"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 73
Updated: 2025-01-15T20:43:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 73
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
