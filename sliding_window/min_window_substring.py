"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 742
Updated: 2025-07-20T21:52:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 742
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
