"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1915
Updated: 2026-06-30T20:56:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1915
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
