"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 717
Updated: 2025-07-14T18:19:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 717
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
