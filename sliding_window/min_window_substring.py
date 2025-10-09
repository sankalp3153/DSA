"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1041
Updated: 2025-10-09T19:13:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1041
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
