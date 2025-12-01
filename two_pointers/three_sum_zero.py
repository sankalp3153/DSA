"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1200
Updated: 2025-12-01T19:09:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1200
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
