"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 2352
Updated: 2026-11-16T19:17:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2352
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
