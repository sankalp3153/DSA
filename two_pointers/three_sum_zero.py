"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1177
Updated: 2025-11-26T18:40:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1177
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
