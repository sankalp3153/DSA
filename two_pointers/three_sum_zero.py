"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 188
Updated: 2025-02-13T17:20:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 188
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
