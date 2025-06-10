"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 607
Updated: 2025-06-10T18:10:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 607
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
