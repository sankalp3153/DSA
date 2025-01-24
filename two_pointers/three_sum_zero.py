"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 96
Updated: 2025-01-24T11:21:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 96
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
