"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1156
Updated: 2025-11-23T18:08:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1156
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
