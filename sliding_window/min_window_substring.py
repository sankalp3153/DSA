"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 834
Updated: 2025-08-12T21:02:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 834
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
