"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 167
Updated: 2025-02-07T21:06:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 167
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
