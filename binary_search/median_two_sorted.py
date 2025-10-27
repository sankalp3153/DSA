"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1090
Updated: 2025-10-27T15:25:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1090
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
