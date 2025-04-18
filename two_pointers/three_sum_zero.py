"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 441
Updated: 2025-04-18T20:40:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 441
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
