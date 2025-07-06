"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 699
Updated: 2025-07-06T20:48:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 699
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
