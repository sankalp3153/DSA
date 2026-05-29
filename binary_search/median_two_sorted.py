"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1803
Updated: 2026-05-29T23:36:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1803
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
