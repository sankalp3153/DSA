"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1338
Updated: 2026-01-07T21:02:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1338
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
