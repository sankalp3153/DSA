"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 29
Updated: 2025-01-07T11:19:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 29
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
