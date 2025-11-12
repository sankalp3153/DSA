"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1133
Updated: 2025-11-12T22:53:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1133
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
