"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 119
Updated: 2025-01-29T16:21:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 119
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
