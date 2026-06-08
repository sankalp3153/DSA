"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1846
Updated: 2026-06-08T21:26:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1846
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
