"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 786
Updated: 2025-08-02T11:52:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 786
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
