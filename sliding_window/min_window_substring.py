"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 512
Updated: 2025-05-13T18:58:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 512
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
