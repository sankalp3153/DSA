"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1363
Updated: 2026-01-16T12:18:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1363
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
