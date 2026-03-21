"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1596
Updated: 2026-03-21T20:32:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1596
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
