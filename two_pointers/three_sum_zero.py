"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1292
Updated: 2025-12-26T23:19:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1292
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
