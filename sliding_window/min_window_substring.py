"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1662
Updated: 2026-04-11T13:15:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1662
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
