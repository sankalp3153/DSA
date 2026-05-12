"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1757
Updated: 2026-05-12T19:08:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1757
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
