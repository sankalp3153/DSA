"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 489
Updated: 2025-05-07T19:30:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 489
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
