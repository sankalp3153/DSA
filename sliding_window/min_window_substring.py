"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1018
Updated: 2025-10-02T15:38:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1018
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
