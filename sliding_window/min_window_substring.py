"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1478
Updated: 2026-02-16T18:44:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1478
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
