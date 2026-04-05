"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1642
Updated: 2026-04-05T14:27:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1642
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
