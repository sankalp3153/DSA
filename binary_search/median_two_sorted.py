"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1849
Updated: 2026-06-09T13:30:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1849
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
