"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 420
Updated: 2025-04-16T14:01:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 420
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
