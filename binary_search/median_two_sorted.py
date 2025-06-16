"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 630
Updated: 2025-06-16T10:50:40+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 630
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
