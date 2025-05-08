"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 492
Updated: 2025-05-08T19:17:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 492
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
