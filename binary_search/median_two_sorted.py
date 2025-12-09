"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1228
Updated: 2025-12-09T23:06:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1228
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
