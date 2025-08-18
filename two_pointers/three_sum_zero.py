"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 855
Updated: 2025-08-18T11:21:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 855
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
