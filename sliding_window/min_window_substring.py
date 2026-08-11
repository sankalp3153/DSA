"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 2053
Updated: 2026-08-11T13:45:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2053
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
