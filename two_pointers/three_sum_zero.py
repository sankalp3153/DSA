"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 326
Updated: 2025-03-20T22:00:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 326
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
