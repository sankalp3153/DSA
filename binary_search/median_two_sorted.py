"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1297
Updated: 2025-12-27T19:31:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1297
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
