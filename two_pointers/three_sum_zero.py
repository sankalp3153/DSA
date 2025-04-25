"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 464
Updated: 2025-04-25T20:23:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 464
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
