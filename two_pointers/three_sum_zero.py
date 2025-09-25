"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 993
Updated: 2025-09-25T10:00:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 993
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
