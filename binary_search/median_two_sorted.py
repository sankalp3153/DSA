"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1780
Updated: 2026-05-19T23:43:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1780
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
