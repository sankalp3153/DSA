"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1984
Updated: 2026-07-19T20:07:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1984
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
