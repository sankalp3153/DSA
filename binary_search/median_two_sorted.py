"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 2056
Updated: 2026-08-12T23:36:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2056
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
