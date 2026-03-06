"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1547
Updated: 2026-03-06T12:02:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1547
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
