"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 2145
Updated: 2026-09-02T13:46:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2145
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
