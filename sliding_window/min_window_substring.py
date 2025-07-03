"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 696
Updated: 2025-07-03T15:48:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 696
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
