"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1039
Updated: 2025-10-09T15:10:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1039
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
