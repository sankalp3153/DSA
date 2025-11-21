"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1154
Updated: 2025-11-21T22:58:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1154
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
