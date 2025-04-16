"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 423
Updated: 2025-04-16T17:21:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 423
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
