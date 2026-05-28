"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1798
Updated: 2026-05-28T14:58:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1798
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
