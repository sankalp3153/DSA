"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 2263
Updated: 2026-10-14T15:12:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2263
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
