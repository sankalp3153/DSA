"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1639
Updated: 2026-04-03T18:02:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1639
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
