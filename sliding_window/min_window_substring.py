"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 880
Updated: 2025-08-24T12:22:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 880
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
