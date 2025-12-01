"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1202
Updated: 2025-12-01T23:29:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1202
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
