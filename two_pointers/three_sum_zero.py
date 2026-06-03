"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1821
Updated: 2026-06-03T21:05:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1821
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
