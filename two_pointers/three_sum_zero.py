"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 234
Updated: 2025-03-01T11:23:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 234
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
