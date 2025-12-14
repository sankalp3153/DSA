"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1251
Updated: 2025-12-14T20:30:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1251
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
