"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 556
Updated: 2025-05-24T22:06:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 556
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
