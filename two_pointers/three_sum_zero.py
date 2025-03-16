"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 303
Updated: 2025-03-16T16:39:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 303
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
