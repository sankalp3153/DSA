"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 765
Updated: 2025-07-26T23:28:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 765
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
