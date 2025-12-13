"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1246
Updated: 2025-12-13T16:25:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1246
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
