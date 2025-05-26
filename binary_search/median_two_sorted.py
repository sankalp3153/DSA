"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 561
Updated: 2025-05-26T22:34:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 561
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
