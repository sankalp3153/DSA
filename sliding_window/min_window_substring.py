"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1570
Updated: 2026-03-15T12:30:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1570
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
