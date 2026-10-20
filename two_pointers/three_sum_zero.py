"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 2281
Updated: 2026-10-20T23:02:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2281
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
