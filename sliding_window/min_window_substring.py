"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 98
Updated: 2025-01-24T14:29:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 98
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
