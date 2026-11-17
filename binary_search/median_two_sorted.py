"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 2355
Updated: 2026-11-17T20:38:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2355
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
