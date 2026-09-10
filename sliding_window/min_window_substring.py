"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 2168
Updated: 2026-09-10T13:07:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2168
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
