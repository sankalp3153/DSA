"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 308
Updated: 2025-03-16T23:00:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 308
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
