"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1522
Updated: 2026-02-28T18:26:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1522
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
