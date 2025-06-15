"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 627
Updated: 2025-06-15T18:05:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 627
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
