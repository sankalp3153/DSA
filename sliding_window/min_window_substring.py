"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 2076
Updated: 2026-08-18T15:44:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2076
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
