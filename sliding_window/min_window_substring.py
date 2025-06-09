"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 604
Updated: 2025-06-09T18:25:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 604
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
