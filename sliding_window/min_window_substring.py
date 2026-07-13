"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1961
Updated: 2026-07-13T18:15:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1961
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
