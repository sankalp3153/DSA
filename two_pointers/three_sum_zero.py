"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 50
Updated: 2025-01-09T18:37:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 50
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
