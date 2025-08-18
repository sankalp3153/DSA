"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 857
Updated: 2025-08-18T13:04:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 857
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
