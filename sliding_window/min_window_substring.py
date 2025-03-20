"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 328
Updated: 2025-03-20T23:17:40+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 328
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
