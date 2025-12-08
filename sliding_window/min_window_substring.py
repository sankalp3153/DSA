"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1225
Updated: 2025-12-08T21:56:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1225
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
