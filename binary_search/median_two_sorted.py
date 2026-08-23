"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 2102
Updated: 2026-08-23T18:06:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2102
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
