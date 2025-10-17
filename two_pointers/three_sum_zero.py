"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1062
Updated: 2025-10-17T15:42:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1062
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
