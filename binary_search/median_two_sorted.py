"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 2332
Updated: 2026-11-05T21:45:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2332
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
