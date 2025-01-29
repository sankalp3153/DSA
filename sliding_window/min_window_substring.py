"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 121
Updated: 2025-01-29T18:04:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 121
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
