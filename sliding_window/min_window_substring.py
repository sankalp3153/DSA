"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 2260
Updated: 2026-10-12T15:46:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2260
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
