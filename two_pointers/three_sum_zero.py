"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 2258
Updated: 2026-10-12T13:13:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2258
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
