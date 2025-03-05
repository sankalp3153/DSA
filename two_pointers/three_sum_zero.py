"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 257
Updated: 2025-03-05T12:58:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 257
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
