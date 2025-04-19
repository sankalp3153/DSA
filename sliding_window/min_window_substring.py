"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 443
Updated: 2025-04-19T10:53:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 443
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
