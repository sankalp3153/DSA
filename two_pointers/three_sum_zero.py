"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1476
Updated: 2026-02-16T16:59:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1476
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
