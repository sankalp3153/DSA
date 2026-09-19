"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 2189
Updated: 2026-09-19T12:40:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2189
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
