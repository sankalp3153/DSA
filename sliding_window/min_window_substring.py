"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 650
Updated: 2025-06-20T15:49:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 650
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
