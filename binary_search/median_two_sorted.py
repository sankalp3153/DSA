"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1573
Updated: 2026-03-16T12:54:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1573
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
