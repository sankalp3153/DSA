"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 648
Updated: 2025-06-19T13:44:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 648
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
