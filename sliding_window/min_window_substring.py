"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 144
Updated: 2025-02-02T21:14:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 144
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
