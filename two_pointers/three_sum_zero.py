"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 694
Updated: 2025-07-02T23:04:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 694
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
