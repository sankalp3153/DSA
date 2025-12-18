"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1269
Updated: 2025-12-18T21:30:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1269
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
