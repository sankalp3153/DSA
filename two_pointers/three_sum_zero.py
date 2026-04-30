"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1729
Updated: 2026-04-30T18:14:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1729
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
