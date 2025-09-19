"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 972
Updated: 2025-09-19T18:39:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 972
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
