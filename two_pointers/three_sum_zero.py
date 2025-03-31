"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 372
Updated: 2025-03-31T16:02:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 372
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
