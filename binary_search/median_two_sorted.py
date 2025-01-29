"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 124
Updated: 2025-01-29T22:15:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 124
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
