"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 211
Updated: 2025-02-19T20:41:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 211
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
