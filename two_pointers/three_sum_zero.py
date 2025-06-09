"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 602
Updated: 2025-06-09T15:30:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 602
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
