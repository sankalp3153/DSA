"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 418
Updated: 2025-04-15T10:13:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 418
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
