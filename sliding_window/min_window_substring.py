"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1087
Updated: 2025-10-26T19:28:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1087
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
