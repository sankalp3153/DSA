"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1734
Updated: 2026-05-04T14:47:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1734
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
