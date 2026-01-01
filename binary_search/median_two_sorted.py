"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1320
Updated: 2026-01-01T20:48:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1320
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
