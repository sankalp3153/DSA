"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 32
Updated: 2025-01-07T17:21:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 32
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
