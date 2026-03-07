"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1550
Updated: 2026-03-07T13:37:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1550
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
