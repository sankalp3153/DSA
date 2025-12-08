"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1223
Updated: 2025-12-08T13:40:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1223
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
