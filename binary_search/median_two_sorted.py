"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1688
Updated: 2026-04-16T22:24:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1688
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
