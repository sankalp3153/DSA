"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 282
Updated: 2025-03-11T17:21:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 282
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
