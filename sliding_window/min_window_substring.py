"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 466
Updated: 2025-04-28T13:32:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 466
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
