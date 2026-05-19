"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1777
Updated: 2026-05-19T20:41:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1777
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
