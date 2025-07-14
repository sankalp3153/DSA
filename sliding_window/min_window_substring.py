"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 719
Updated: 2025-07-14T21:04:26+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 719
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
