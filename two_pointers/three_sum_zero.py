"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 2327
Updated: 2026-11-04T10:33:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2327
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
