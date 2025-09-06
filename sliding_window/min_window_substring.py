"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 926
Updated: 2025-09-06T11:12:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 926
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
