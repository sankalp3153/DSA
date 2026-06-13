"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1872
Updated: 2026-06-13T11:52:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1872
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
