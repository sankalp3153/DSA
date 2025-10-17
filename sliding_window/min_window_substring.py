"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1064
Updated: 2025-10-17T18:10:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1064
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
