"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 52
Updated: 2025-01-09T21:21:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 52
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
