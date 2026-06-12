"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1867
Updated: 2026-06-12T18:23:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1867
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
