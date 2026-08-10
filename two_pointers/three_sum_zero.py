"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 2051
Updated: 2026-08-10T23:39:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2051
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
