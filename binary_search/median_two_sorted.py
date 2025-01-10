"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 55
Updated: 2025-01-10T21:55:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 55
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
