"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 1708
Updated: 2026-04-24T12:19:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1708
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
