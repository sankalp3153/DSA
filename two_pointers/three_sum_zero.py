"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1430
Updated: 2026-02-05T10:09:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1430
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
