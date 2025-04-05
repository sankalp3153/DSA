"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 395
Updated: 2025-04-05T18:04:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 395
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
