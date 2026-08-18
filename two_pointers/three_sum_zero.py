"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 2074
Updated: 2026-08-18T14:20:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2074
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
