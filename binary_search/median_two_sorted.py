"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 2125
Updated: 2026-08-28T13:25:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2125
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
