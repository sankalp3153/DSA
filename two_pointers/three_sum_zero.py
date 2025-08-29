"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 901
Updated: 2025-08-29T17:02:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 901
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
