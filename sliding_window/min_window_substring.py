"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 558
Updated: 2025-05-25T17:06:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 558
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
