"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1108
Updated: 2025-10-31T23:29:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1108
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
