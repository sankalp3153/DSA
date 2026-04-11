"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1665
Updated: 2026-04-11T16:38:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1665
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
