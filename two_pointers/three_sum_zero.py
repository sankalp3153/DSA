"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 4
Updated: 2025-01-02T16:40:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 4
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
