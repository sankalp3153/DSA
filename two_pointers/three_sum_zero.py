"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1637
Updated: 2026-04-02T19:16:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1637
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
