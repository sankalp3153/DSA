"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1685
Updated: 2026-04-16T13:25:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1685
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
