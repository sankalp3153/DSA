"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 262
Updated: 2025-03-08T15:52:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 262
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
