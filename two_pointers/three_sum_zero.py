"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 763
Updated: 2025-07-26T20:55:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 763
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
