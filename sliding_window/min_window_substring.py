"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 2191
Updated: 2026-09-19T14:03:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2191
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
