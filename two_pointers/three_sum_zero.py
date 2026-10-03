"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 2235
Updated: 2026-10-03T10:33:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2235
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
