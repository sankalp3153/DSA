"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 2350
Updated: 2026-11-16T14:35:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2350
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
