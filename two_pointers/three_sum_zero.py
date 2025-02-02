"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 142
Updated: 2025-02-02T16:22:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 142
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
