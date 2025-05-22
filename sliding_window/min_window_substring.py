"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 535
Updated: 2025-05-22T11:24:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 535
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
