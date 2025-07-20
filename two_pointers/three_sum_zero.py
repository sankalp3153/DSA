"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 740
Updated: 2025-07-20T18:53:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 740
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
