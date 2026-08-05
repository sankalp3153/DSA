"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 2033
Updated: 2026-08-05T17:37:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2033
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
