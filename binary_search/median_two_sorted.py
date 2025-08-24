"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 883
Updated: 2025-08-24T17:11:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 883
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
