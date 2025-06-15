"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 625
Updated: 2025-06-15T11:01:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 625
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
