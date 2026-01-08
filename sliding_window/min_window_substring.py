"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1340
Updated: 2026-01-08T11:26:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1340
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
