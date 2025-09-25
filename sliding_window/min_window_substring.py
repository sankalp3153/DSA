"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 995
Updated: 2025-09-25T16:48:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 995
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
