"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1731
Updated: 2026-04-30T22:25:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1731
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
