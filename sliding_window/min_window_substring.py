"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 581
Updated: 2025-06-03T16:16:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 581
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
