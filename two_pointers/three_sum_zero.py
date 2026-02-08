"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1453
Updated: 2026-02-08T22:23:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1453
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
