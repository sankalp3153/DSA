"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 673
Updated: 2025-06-26T20:18:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 673
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
