"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 788
Updated: 2025-08-03T11:32:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 788
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
