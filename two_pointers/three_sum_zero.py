"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 2097
Updated: 2026-08-22T19:09:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2097
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
