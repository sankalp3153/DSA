"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1754
Updated: 2026-05-09T23:12:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1754
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
