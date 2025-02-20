"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 213
Updated: 2025-02-20T13:44:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 213
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
