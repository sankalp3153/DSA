"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 2010
Updated: 2026-07-28T17:22:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2010
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
