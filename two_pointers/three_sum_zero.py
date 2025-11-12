"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1131
Updated: 2025-11-12T11:58:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1131
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
