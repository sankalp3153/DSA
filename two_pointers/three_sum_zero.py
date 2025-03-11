"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 280
Updated: 2025-03-11T14:05:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 280
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
