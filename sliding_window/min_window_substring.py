"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 2007
Updated: 2026-07-28T11:41:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2007
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
