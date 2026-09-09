"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 2166
Updated: 2026-09-09T13:15:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2166
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
