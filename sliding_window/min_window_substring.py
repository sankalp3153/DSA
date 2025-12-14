"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1248
Updated: 2025-12-14T15:29:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1248
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
