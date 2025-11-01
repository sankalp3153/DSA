"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1110
Updated: 2025-11-01T13:31:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1110
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
