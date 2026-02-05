"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1432
Updated: 2026-02-05T11:39:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1432
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
