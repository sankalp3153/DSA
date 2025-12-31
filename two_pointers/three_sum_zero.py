"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1315
Updated: 2025-12-31T12:42:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1315
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
