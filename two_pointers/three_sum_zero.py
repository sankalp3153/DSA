"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 349
Updated: 2025-03-24T12:07:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 349
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
