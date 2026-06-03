"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1823
Updated: 2026-06-03T21:50:26+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1823
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
