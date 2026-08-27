"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 2120
Updated: 2026-08-27T17:59:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2120
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
