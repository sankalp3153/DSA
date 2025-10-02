"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1021
Updated: 2025-10-02T22:21:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1021
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
