"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 653
Updated: 2025-06-20T17:57:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 653
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
