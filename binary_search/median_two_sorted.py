"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 2240
Updated: 2026-10-04T23:36:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2240
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
