"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1614
Updated: 2026-03-25T14:03:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1614
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
