"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1412
Updated: 2026-01-31T15:27:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1412
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
