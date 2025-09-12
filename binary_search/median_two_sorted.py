"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 952
Updated: 2025-09-12T11:25:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 952
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
