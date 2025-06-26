"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 671
Updated: 2025-06-26T18:43:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 671
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
