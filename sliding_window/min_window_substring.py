"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1271
Updated: 2025-12-18T23:14:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1271
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
