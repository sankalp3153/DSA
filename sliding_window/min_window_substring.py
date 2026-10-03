"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 2237
Updated: 2026-10-03T18:00:40+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2237
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
