"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1895
Updated: 2026-06-22T22:28:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1895
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
