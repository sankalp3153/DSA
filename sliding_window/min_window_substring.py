"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1294
Updated: 2025-12-27T10:50:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1294
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
