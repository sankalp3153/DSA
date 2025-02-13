"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 190
Updated: 2025-02-13T22:53:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 190
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
