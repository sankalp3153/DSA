"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 351
Updated: 2025-03-25T15:55:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 351
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
