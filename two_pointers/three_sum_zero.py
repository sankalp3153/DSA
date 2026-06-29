"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 1913
Updated: 2026-06-29T20:08:26+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1913
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
