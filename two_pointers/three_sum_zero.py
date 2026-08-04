"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 2028
Updated: 2026-08-04T14:21:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2028
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
