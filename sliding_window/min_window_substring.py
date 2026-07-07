"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1938
Updated: 2026-07-07T14:05:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1938
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
