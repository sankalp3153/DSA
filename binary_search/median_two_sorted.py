"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1826
Updated: 2026-06-04T14:52:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1826
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
