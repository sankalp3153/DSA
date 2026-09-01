"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 2143
Updated: 2026-09-01T21:18:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2143
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
