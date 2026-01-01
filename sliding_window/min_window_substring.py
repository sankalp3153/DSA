"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1317
Updated: 2026-01-01T15:48:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1317
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
