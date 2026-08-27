"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 2122
Updated: 2026-08-27T20:54:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2122
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
