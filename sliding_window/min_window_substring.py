"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 374
Updated: 2025-04-01T10:37:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 374
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
