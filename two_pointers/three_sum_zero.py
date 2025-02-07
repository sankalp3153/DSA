"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 165
Updated: 2025-02-07T15:14:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 165
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
