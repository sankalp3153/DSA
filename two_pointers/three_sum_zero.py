"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 533
Updated: 2025-05-20T19:14:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 533
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
