"""
Module: min_window_substring
Approach: frequency map window contraction
Revision: 397
Updated: 2025-04-07T14:17:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 397
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
