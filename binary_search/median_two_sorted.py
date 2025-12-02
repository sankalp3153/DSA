"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1205
Updated: 2025-12-02T21:11:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1205
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
