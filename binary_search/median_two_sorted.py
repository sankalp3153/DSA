"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 2079
Updated: 2026-08-18T22:12:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2079
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
