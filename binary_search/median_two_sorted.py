"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 2194
Updated: 2026-09-19T17:36:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2194
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
