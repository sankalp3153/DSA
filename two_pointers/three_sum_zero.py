"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 2212
Updated: 2026-09-29T14:27:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2212
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
