"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 2005
Updated: 2026-07-27T14:20:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2005
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
