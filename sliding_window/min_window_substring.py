"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1593
Updated: 2026-03-21T14:50:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1593
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
