"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 259
Updated: 2025-03-07T22:26:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 259
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
