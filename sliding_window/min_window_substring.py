"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 75
Updated: 2025-01-16T13:39:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 75
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
