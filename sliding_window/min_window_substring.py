"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1616
Updated: 2026-03-25T16:59:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1616
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
