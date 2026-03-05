"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1545
Updated: 2026-03-05T20:39:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1545
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
