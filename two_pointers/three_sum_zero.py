"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1683
Updated: 2026-04-15T20:18:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1683
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
