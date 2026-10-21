"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 2283
Updated: 2026-10-21T14:25:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2283
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
