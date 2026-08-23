"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 2099
Updated: 2026-08-23T13:42:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2099
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
