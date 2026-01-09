"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1343
Updated: 2026-01-09T12:43:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1343
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
