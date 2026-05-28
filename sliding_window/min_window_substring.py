"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1800
Updated: 2026-05-28T20:26:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1800
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
