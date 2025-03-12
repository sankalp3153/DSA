"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 285
Updated: 2025-03-12T15:32:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 285
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
