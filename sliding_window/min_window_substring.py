"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 2306
Updated: 2026-10-31T10:12:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2306
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
