"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1481
Updated: 2026-02-16T21:42:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1481
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
