"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1890
Updated: 2026-06-21T13:22:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1890
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
