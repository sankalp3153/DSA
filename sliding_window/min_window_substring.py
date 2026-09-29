"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 2214
Updated: 2026-09-29T15:58:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2214
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
