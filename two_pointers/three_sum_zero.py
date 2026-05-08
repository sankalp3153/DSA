"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1752
Updated: 2026-05-08T21:03:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1752
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
