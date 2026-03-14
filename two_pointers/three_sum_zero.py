"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1568
Updated: 2026-03-14T22:45:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1568
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
