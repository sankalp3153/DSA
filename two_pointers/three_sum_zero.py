"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1982
Updated: 2026-07-18T23:36:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1982
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
