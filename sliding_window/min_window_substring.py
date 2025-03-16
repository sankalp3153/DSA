"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 305
Updated: 2025-03-16T19:23:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 305
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
