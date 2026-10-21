"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 2286
Updated: 2026-10-21T21:45:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2286
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
