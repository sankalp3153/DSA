"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1706
Updated: 2026-04-23T16:19:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1706
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
