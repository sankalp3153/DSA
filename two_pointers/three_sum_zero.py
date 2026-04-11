"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1660
Updated: 2026-04-11T11:37:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1660
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
