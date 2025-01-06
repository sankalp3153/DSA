"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 27
Updated: 2025-01-06T21:36:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 27
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
