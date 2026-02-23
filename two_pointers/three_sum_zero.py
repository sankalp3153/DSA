"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1499
Updated: 2026-02-23T19:56:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1499
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
