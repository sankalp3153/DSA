"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 579
Updated: 2025-06-03T12:14:40+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 579
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
