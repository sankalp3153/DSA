"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1869
Updated: 2026-06-13T10:16:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1869
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
