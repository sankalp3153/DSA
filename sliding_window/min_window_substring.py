"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1501
Updated: 2026-02-25T12:46:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1501
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
