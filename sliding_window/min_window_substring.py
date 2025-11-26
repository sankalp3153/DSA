"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1179
Updated: 2025-11-26T19:08:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1179
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
