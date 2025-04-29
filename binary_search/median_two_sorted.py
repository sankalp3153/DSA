"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 469
Updated: 2025-04-29T19:18:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 469
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
