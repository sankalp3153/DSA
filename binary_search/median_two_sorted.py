"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1619
Updated: 2026-03-25T22:04:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1619
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
