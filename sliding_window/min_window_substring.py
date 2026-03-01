"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1524
Updated: 2026-03-01T16:26:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1524
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
