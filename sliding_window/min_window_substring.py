"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 236
Updated: 2025-03-01T17:06:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 236
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
