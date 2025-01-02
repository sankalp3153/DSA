"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 6
Updated: 2025-01-02T22:56:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 6
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
