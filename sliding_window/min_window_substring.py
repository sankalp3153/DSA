"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 811
Updated: 2025-08-09T15:39:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 811
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
