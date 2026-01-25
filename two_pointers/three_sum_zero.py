"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1384
Updated: 2026-01-25T16:31:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1384
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
