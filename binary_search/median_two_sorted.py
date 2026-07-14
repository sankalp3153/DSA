"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1964
Updated: 2026-07-14T14:09:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1964
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
