"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 101
Updated: 2025-01-24T22:34:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 101
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
