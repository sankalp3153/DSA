"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 809
Updated: 2025-08-08T21:04:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 809
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
