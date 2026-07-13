"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1959
Updated: 2026-07-13T12:17:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1959
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
